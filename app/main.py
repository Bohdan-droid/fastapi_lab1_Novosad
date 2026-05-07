from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.categories import router as categories_router
from app.api.products import router as products_router
from app.api.profiles import router as profiles_router
from app.api.orders import router as orders_router

app = FastAPI(title="Novosad Lab API")

# Підключаємо всі роутери
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(profiles_router)
app.include_router(orders_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Lab 4 API"}