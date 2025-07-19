from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr

class ReminderCreate(BaseModel):
    name: str
    email: EmailStr

class ReminderRead(BaseModel):
    id: int
    name: str
    email: EmailStr

class ReminderUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr
