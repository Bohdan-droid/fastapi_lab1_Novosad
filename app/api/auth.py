from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate  # використаємо для прикладу, або створи окрему UserLogin
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(
    response: Response,
    user_data: UserCreate, # Користувач вводить email та password
    db: AsyncSession = Depends(get_db)
):
    # 1. Шукаємо юзера
    result = await db.execute(select(User).where(User.email == user_data.email))
    user = result.scalar_one_or_none()

    # 2. Перевіряємо пароль
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # 3. Генеруємо JWT токен
    token = create_access_token(data={"sub": user.email})

    # 4. Встановлюємо КУКІ
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True, # Захист від крадіжки токена скриптами
        samesite="lax"
    )

    return {"message": "Successfully logged in"}