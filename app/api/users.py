from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

# Емуляція бази даних
fake_users_db = {}
current_id = 1


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    global current_id
    new_user = {"id": current_id, **user.dict()}
    fake_users_db[current_id] = new_user
    current_id += 1
    return new_user


@router.get("/", response_model=List[UserResponse])
def get_all_users():
    return list(fake_users_db.values())


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[user_id]


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user_data = fake_users_db[user_id]
    update_data = user_update.dict(exclude_unset=True)
    updated_user = {**stored_user_data, **update_data}

    fake_users_db[user_id] = updated_user
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[user_id]
    return {"message": "User deleted successfully"}