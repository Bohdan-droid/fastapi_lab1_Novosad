from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    new_category = Category(name=category.name)
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category

@router.get("/", response_model=list[CategoryResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category))
    return list(result.scalars().all())