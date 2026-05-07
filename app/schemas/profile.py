from pydantic import BaseModel, ConfigDict

class ProfileCreate(BaseModel):
    full_name: str
    address: str
    user_id: int

class ProfileResponse(BaseModel):
    id: int
    full_name: str
    address: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)