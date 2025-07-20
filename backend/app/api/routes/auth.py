from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session
from app.models.db.postgres import User
from app.models.requests.auth import RegisterUser, LoginRequest, OTPVerificationRequest
from app.api.deps import get_db, get_redis
from app import email_utils
import random
import asyncio

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register")
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.email == user.email) | (User.phone_number == user.phone_number)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email or phone number already registered")
    
    db.add(user)
    db.commit()
    return {"success": True, "message": "User registered successfully"}

@router.post("/login/send_otp")
async def login_send_otp(data: LoginRequest, db: Session = Depends(get_db), otp_store=Depends(get_redis)):
    email = data.email
    otp = str(random.randint(100000, 999999))
    await otp_store.set(f"{email}", otp, ex=300)

    try:
        email_utils.send_otp_email(email, otp, "Login")
        return {"success": True, "message": "OTP sent successfully to email."}
    except Exception as e:
        return {"success": False, "message": str(e)}

@router.post("/login/verify_otp")
async def login_verify_otp(data: OTPVerificationRequest, db: Session = Depends(get_db), otp_store=Depends(get_redis)):
    email = data.email
    user_otp = data.otp
    stored_otp = otp_store.get(f"{email}")

    if stored_otp is None:
        raise HTTPException(status_code=400, detail="OTP expired or not found")
    if stored_otp != user_otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    await otp_store.delete(f"{email}")

    role = None
    user = db.query(User).filter(User.email == email).first()

    if user:
        if 'admin' in email:  # setting manually for admin
            role = 'admin'
        else:
            role = 'user'

    if not role:
        return {"success": False, "message": "User not found."}

    return {"success": True, "role": role}