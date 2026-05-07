from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Параметри бази даних
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Секретний ключ для JWT (тепер береться з .env)
    SECRET_KEY: str

    # Вказуємо Pydantic читати файл .env та ігнорувати зайві змінні
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()