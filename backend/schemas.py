from pydantic import BaseModel, EmailStr
from typing import Optional

class RegistrationRequest(BaseModel):
    senior_name: str
    senior_email: EmailStr
    senior_dob: str
    senior_gender: str
    senior_mobile: Optional[str]
    child_name: str
    child_email: EmailStr
    child_mobile: Optional[str]

class OTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str

class EmailRequest(BaseModel):
    email: EmailStr

class OTPVerification(BaseModel):
    email: EmailStr
    otp: str