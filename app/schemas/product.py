from pydantic import BaseModel, ConfigDict

class ProductCreate(BaseModel):
    title: str
    price: float
    category_id: int

class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    category_id: int
    model_config = ConfigDict(from_attributes=True)