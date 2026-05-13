from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator  # ДОДАНО
from app.api.users import router as users_router
from app.api.categories import router as categories_router
from app.api.products import router as products_router
from app.api.profiles import router as profiles_router
from app.api.orders import router as orders_router
from app.api.auth import router as auth_router

app = FastAPI(title="Novosad Lab 7 API (Grafana & Prometheus)")

# Підключаємо всі роутери
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(profiles_router)
app.include_router(orders_router)

# ДОДАНО: Ініціалізація збору метрик для Prometheus
# Цей код автоматично створить ручку /metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Welcome to Lab 7 API (Metrics enabled)"}