from fastapi import Request, HTTPException, status
from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM

async def get_current_user_email(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")