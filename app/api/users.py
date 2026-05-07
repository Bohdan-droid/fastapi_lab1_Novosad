from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


# 1. CREATE: Створення користувача
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Перевірка, чи не зайнятий username
    result = await db.execute(select(User).where(User.username == user.username))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=user.username, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


# 2. READ: Отримання всіх користувачів
@router.get("/", response_model=list[UserResponse])
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return list(result.scalars().all())


# 3. READ: Отримання одного користувача за ID
@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 4. UPDATE: Оновлення користувача
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = user_data.username
    user.email = user_data.email
    await db.commit()
    await db.refresh(user)
    return user


# 5. DELETE: Видалення користувача
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()