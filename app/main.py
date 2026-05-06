from fastapi import FastAPI
from app.api.users import router as users_router

app = FastAPI(title="Lab 3 CRUD Users")

# Підключаємо наш роутер
app.include_router(users_router)