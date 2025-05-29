import base64

import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from domain.user import User
from infrastructure.config import settings
from infrastructure.mongodb import get_engine

security = HTTPBearer()

# 這些值應該從環境變量中讀取
OIDC_ISSUER = settings.OIDC_ISSUER
OIDC_AUDIENCE = settings.OIDC_AUDIENCE


def int_from_base64url(b64urlstring):
    """將 base64url 編碼的字符串轉換為整數"""
    return int.from_bytes(
        base64.urlsafe_b64decode(b64urlstring + '=' * (4 - len(b64urlstring) % 4)),
        'big',
    )


def get_public_key():
    """從 Keycloak 獲取公鑰"""
    try:
        # 從 Keycloak 的 OpenID Configuration 獲取 JWKS 端點
        config_url = f'{OIDC_ISSUER}/.well-known/openid-configuration'
        config = requests.get(config_url).json()
        jwks_url = config['jwks_uri']

        # 獲取 JWKS
        jwks = requests.get(jwks_url).json()

        # 找到用於簽名的密鑰（use="sig"）
        for key in jwks['keys']:
            if key['use'] == 'sig':
                # 將 JWK 轉換為 PEM 格式
                numbers = RSAPublicNumbers(
                    e=int_from_base64url(key['e']), n=int_from_base64url(key['n'])
                )
                public_key = numbers.public_key(backend=default_backend())
                pem = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
                return pem

        raise Exception('No signing key found')
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get public key: {str(e)}',
        )


async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    try:
        token = credentials.credentials
        # 獲取公鑰
        public_key = get_public_key()

        # 驗證 token
        payload = jwt.decode(
            token,
            public_key,
            options={'verify_signature': True},
            audience=OIDC_AUDIENCE,
            issuer=OIDC_ISSUER,
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Invalid authentication credentials: {str(e)}',
            headers={'WWW-Authenticate': 'Bearer'},
        )


# 用於獲取當前用戶的依賴
async def get_current_user(request: Request, payload: dict = Depends(verify_token)) -> dict:
    # 獲取用戶信息
    user_info = {
        'sub': payload.get('sub'),
        'email': payload.get('email'),
        'name': payload.get('name') or payload.get('preferred_username'),
        'preferred_username': payload.get('preferred_username'),
        'realm_access': payload.get('realm_access', {}).get('roles', []),
    }

    # 檢查必要欄位
    if not user_info['sub'] or not user_info['email'] or not user_info['name']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Missing required user information in token',
        )

    # 檢查用戶是否已存在
    engine = get_engine(request.app)
    existing_user = await engine.find_one(User, User.user_sub == user_info['sub'])

    # 如果用戶不存在，創建新用戶
    if not existing_user:
        new_user = User(
            user_sub=user_info['sub'],
            user_email=user_info['email'],
            user_name=user_info['name'],
            user_is_teacher=False,
        )
        await engine.save(new_user)
    # Return the user object (or a dict representation)
    # For consistency with get_current_user, returning user_info dict for now.
    # If User object is preferred, change return type and this line.
    return user_info # or existing_user or new_user


async def validate_id_token(id_token_str: str) -> dict:
    """驗證 ID Token 並返回 payload"""
    try:
        public_key = get_public_key()
        payload = jwt.decode(
            id_token_str,
            public_key,
            options={'verify_signature': True, 'verify_aud': True, 'verify_iss': True, 'verify_exp': True},
            audience=OIDC_AUDIENCE,
            issuer=OIDC_ISSUER,
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Invalid ID token: {str(e)}',
        )
    except Exception as e: # Catch other potential errors during validation
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'An error occurred during ID token validation: {str(e)}',
        )

async def find_or_create_user_from_token_payload(payload: dict, request: Request) -> User: # Return type User
    """根據 token payload 查找或創建用戶，返回 User 對象"""
    user_info = {
        'sub': payload.get('sub'),
        'email': payload.get('email'),
        'name': payload.get('name') or payload.get('preferred_username'),
        # Add any other fields you want to sync from the token
    }

    if not user_info['sub'] or not user_info['email'] or not user_info['name']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Missing required user information in token payload for user processing',
        )

    engine = get_engine(request.app)
    existing_user = await engine.find_one(User, User.user_sub == user_info['sub'])

    if existing_user:
        # Optionally update existing user's fields here if they can change in Keycloak
        # e.g., existing_user.user_email = user_info['email']
        # await engine.save(existing_user)
        return existing_user

    # 如果用戶不存在，創建新用戶
    new_user = User(
        user_sub=user_info['sub'],
        user_email=user_info['email'],
        user_name=user_info['name'],
        user_is_teacher=False, # Default value, adjust as needed
    )
    await engine.save(new_user)
    return new_user

# Refactor get_current_user to use the new function
# 用於獲取當前用戶的依賴
async def get_current_user(request: Request, payload: dict = Depends(verify_token)) -> User: # Return type User
    # The payload is already validated by verify_token
    # Now find or create the user based on this payload
    user_object = await find_or_create_user_from_token_payload(payload, request)
    # Convert User object to dict for backward compatibility if needed by callers,
    # but returning the User object is cleaner.
    # For now, let's return a dict similar to the old get_current_user for minimal interface change.
    # However, the 'find_or_create_user_from_token_payload' returns a User object,
    # so we might need to adjust this or the caller.
    # For this iteration, let's return the dict representation.
    return {
        'sub': user_object.user_sub,
        'email': user_object.user_email,
        'name': user_object.user_name,
        'preferred_username': payload.get('preferred_username'), # Keep this from original payload
        'realm_access': payload.get('realm_access', {}).get('roles', []), # Keep this from original payload
    }


async def exchange_code_for_tokens(code: str, request: Request) -> dict:
    """使用授權碼交換 token"""
    redirect_uri = str(request.base_url).rstrip('/') + "/api/auth/callback"
    # Ensure redirect_uri does not have a trailing slash if base_url is just "http://host:port/"
    # A more robust way might be:
    # parsed_url = urlparse(str(request.base_url))
    # redirect_uri = f"{parsed_url.scheme}://{parsed_url.netloc}/api/auth/callback"
    # However, request.base_url should already handle this correctly.
    # Let's refine the redirect_uri construction slightly to be more robust
    
    # Construct the redirect_uri using request.url_for for robustness if router is named
    # For now, combining base_url and the known path.
    # Ensure no double slashes if request.base_url already ends with a slash
    base_url_str = str(request.base_url)
    if base_url_str.endswith('/'):
        redirect_uri = f"{base_url_str}api/auth/callback"
    else:
        redirect_uri = f"{base_url_str}/api/auth/callback"

    token_url = f"{settings.OIDC_ISSUER}/protocol/openid-connect/token"
    
    payload = {
        'grant_type': 'authorization_code',
        'client_id': settings.OIDC_CLIENT_ID,
        'client_secret': settings.OIDC_CLIENT_SECRET,
        'code': code,
        'redirect_uri': redirect_uri,
    }
    
    try:
        response = requests.post(token_url, data=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        return response.json()
    except requests.exceptions.HTTPError as e:
        # Log the error details from response if possible
        error_detail = f"Failed to exchange code for tokens: {e.response.status_code} - {e.response.text}"
        print(f"Token exchange error: {error_detail}") # Or use a proper logger
        raise HTTPException(
            status_code=e.response.status_code,
            detail=error_detail
        )
    except requests.exceptions.RequestException as e:
        # For other network issues
        error_detail = f"Network error during token exchange: {str(e)}"
        print(f"Token exchange error: {error_detail}") # Or use a proper logger
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error_detail
        )
