from fastapi import APIRouter, Depends, Request, HTTPException, Response
from fastapi.responses import RedirectResponse

from application.auth_service import (
    get_current_user,
    exchange_code_for_tokens,
    validate_id_token,
    find_or_create_user_from_token_payload
)
from domain.user import User # For type hinting if needed

router = APIRouter()

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@router.get("/api/auth/callback")
async def auth_callback(request: Request, response: Response, code: str = None, state: str = None):
    if not code:
        print("Callback called without a code.")
        raise HTTPException(status_code=400, detail="Authorization code not provided")

    print(f"Received callback with code: {code}, state: {state}") # State can be used for CSRF protection
    
    try:
        tokens = await exchange_code_for_tokens(code=code, request=request)
        print(f"Successfully exchanged code for tokens.") # Avoid logging full tokens

        id_token_str = tokens.get("id_token")
        if not id_token_str:
            print("ID token not found in token response.")
            raise HTTPException(status_code=500, detail="ID token not found in token response")

        access_token_str = tokens.get("access_token") # access_token also needed for frontend

        # Validate the ID token
        id_token_payload = await validate_id_token(id_token_str)
        print(f"ID token validated successfully. Payload sub: {id_token_payload.get('sub')}")

        # Find or create user
        # The find_or_create_user_from_token_payload function returns a User object
        user_object = await find_or_create_user_from_token_payload(id_token_payload, request)
        print(f"User processed: {user_object.user_email} (ID: {user_object.id}, SUB: {user_object.user_sub})")

        # TODO: Securely store tokens (e.g., access_token, refresh_token in HTTPOnly cookies)
        # For now, passing them in URL fragment for SPA handling as per common OIDC browser flows.
        # The frontend should clear this from the URL bar.
        
        # Using relative path for redirect. Frontend base URL needs to be configured there.
        # Example: http://localhost:8080/auth/callback#access_token=...&id_token=...
        # The frontend should be configured to handle this path and extract tokens.
        frontend_redirect_url = f"/auth/callback#access_token={access_token_str}&id_token={id_token_str}"
        if tokens.get("refresh_token"): # Include refresh token if available
             frontend_redirect_url += f"&refresh_token={tokens.get('refresh_token')}"
        if state: # Include state if it was part of the initial request
            frontend_redirect_url += f"&state={state}"
            
        print(f"Redirecting to frontend: {frontend_redirect_url}")
        # Use 303 See Other for redirect after POST, but this is a GET callback.
        # 302 Found is common, or 303. Let's use 303 as it implies the new resource is different.
        return RedirectResponse(url=frontend_redirect_url, status_code=303)

    except HTTPException as e:
        print(f"Error during OIDC callback processing: {e.detail}, status: {e.status_code}")
        # Redirect to an error page on the frontend or return a JSON error
        # For now, re-raising to let FastAPI handle it, which will return a JSON error.
        # Consider a redirect to frontend error page: 
        # return RedirectResponse(url=f"/auth/error?message={e.detail}", status_code=303)
        raise e
    except Exception as e:
        print(f"An unexpected error occurred in OIDC callback: {str(e)}")
        # Similar to above, consider redirecting to a generic error page on frontend
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
