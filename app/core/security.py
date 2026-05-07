from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext

# Налаштування хешування
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "SUPER_SECRET_KEY_FOR_BASKETBALL_APP"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)