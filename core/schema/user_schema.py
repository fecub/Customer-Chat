from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    role: str  # "customer" oder "support"

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

