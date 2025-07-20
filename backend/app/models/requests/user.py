from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    gender: Optional[str] = None
    phone_number: str
    is_admin: Optional[bool] = False

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    id: UUID