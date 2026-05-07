from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# Створення рушія (engine)
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Фабрика сесій (session factory)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Функція для отримання сесії (будемо використовувати в роутерах)
async def get_db():
    async with async_session_maker() as session:
        yield session