import base64
import os

import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from domain.user import User
from infrastructure.mongodb import get_engine

security = HTTPBearer()

# 這些值應該從環境變量中讀取
OIDC_ISSUER = os.getenv('OIDC_ISSUER', 'http://172.16.1.16:8081/realms/coder')
OIDC_AUDIENCE = os.getenv('OIDC_AUDIENCE', 'account')


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
    return user_info
