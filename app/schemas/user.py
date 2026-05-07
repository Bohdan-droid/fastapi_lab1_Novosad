from pydantic import BaseModel, EmailStr, ConfigDict

# Схема для реєстрації (тут пароль ПРЯМИМ текстом)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  # Додаємо це поле для реєстрації

# Схема для відповіді (тут пароля НЕМАЄ, навіть хешованого)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)