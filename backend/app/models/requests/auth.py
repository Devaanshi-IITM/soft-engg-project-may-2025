from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    gender: Optional[str] = None
    phone_number: str
    is_admin: Optional[bool] = False

class RegisterUser(UserBase):
    pass

class LoginRequest(BaseModel):
    email: EmailStr

class OTPVerificationRequest(BaseModel):
    otp: str