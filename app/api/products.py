from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from prometheus_client import Counter # ДОДАНО: Імпорт лічильника

from app.db.session import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.api.deps import get_current_user_email

router = APIRouter(prefix="/products", tags=["products"])

# ДОДАНО: Наша кастомна метрика
# Вона рахуватиме загальну суму цін усіх створених товарів
TOTAL_REVENUE = Counter(
    "total_products_revenue",
    "Загальна сума цін усіх створених товарів (Кастомна метрика)"
)

# 1. Створення товару
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user_email: str = Depends(get_current_user_email)
):
    new_product = Product(
        title=product.title,
        price=product.price,
        category_id=product.category_id
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    # ДОДАНО: Збільшуємо наш лічильник на ціну створеного товару
    TOTAL_REVENUE.inc(product.price)

    return new_product

# 2. Отримання товарів
@router.get("/", response_model=list[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    return list(result.scalars().all())