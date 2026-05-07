from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int

class OrderResponse(BaseModel):
    id: int
    created_at: datetime
    user_id: int
    model_config = ConfigDict(from_attributes=True)