from pydantic import BaseModel, EmailStr, ConfigDict

# Схема для отримання даних від клієнта (POST, PUT)
class UserCreate(BaseModel):
    username: str
    email: EmailStr

# Схема для відправки даних клієнту (GET)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    # Дозволяє Pydantic читати дані з моделей SQLAlchemy
    model_config = ConfigDict(from_attributes=True)