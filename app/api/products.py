from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.api.deps import get_current_user_email  # Імпортуємо нашого "охоронця"

router = APIRouter(prefix="/products", tags=["products"])

# 1. Створення товару — ТЕПЕР ЗАХИЩЕНО
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user_email: str = Depends(get_current_user_email) # Вимагаємо вхід
):
    """
    Тільки аутентифіковані користувачі можуть створювати товари.
    Перевірка відбувається автоматично через кукі 'access_token'.
    """
    new_product = Product(
        title=product.title,
        price=product.price,
        category_id=product.category_id
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

# 2. Отримання товарів — залишаємо відкритим (публічним)
@router.get("/", response_model=list[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    return list(result.scalars().all())