from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # НОВЕ ПОЛЕ ДЛЯ ПАРОЛЯ (додаємо сюди)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    # Зв'язок One-to-One з профілем
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)
    # Зв'язок One-to-Many з замовленнями
    orders: Mapped[list["Order"]] = relationship(back_populates="user")