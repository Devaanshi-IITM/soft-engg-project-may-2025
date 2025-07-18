from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import random

from . import models, schemas, email_utils, otp_store, database
from .schemas import EmailRequest, OTPVerification


app = FastAPI()

origins = ["*"]  # Adjust this for production
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/send_otps")
def send_otps(data: schemas.RegistrationRequest):
    senior_otp = str(random.randint(100000, 999999))
    child_otp = str(random.randint(100000, 999999))

    otp_store.otp_store[data.senior_email] = senior_otp
    otp_store.otp_store[data.child_email] = child_otp

    try:
        email_utils.send_otp_email(data.senior_email, senior_otp, "Senior")
        email_utils.send_otp_email(data.child_email, child_otp, "Child")
        return {"success": True, "message": "OTPs sent."}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/verify_and_register")
def verify_and_register(
    data: schemas.RegistrationRequest,
    senior_otp: str,
    child_otp: str,
    db: Session = Depends(get_db)
):
    if otp_store.otp_store.get(data.senior_email) != senior_otp:
        raise HTTPException(status_code=400, detail="Senior OTP invalid.")
    if otp_store.otp_store.get(data.child_email) != child_otp:
        raise HTTPException(status_code=400, detail="Child OTP invalid.")

    new_entry = models.Registration(**data.dict())
    db.add(new_entry)
    db.commit()
    return {"success": True, "message": "Registration successful!"}

@app.post("/login/send_otp")
def login_send_otp(data: EmailRequest):
    email = data.email
    otp = str(random.randint(100000, 999999))
    otp_store.otp_store[email] = otp

    try:
        email_utils.send_otp_email(email, otp, "Login")
        return {"success": True}
    except Exception as e:
        return {"success": False, "message": str(e)}

@app.post("/login/verify_otp")
def login_verify_otp(data: OTPVerification, db: Session = Depends(get_db)):
    email = data.email
    user_otp = data.otp
    stored_otp = otp_store.otp_store.get(email)

    if not stored_otp or stored_otp != user_otp:
        return {"success": False, "message": "Invalid OTP."}

    role = None
    user = db.query(models.Registration).filter(
        (models.Registration.senior_email == email) |
        (models.Registration.child_email == email)
    ).first()

    if user:
        if email == user.senior_email:
            role = 'senior'
        elif email == user.child_email:
            role = 'guardian'
    elif email == "admin@example.com":  # setting manually for admin
        role = 'admin'

    if not role:
        return {"success": False, "message": "User not found."}

    return {"success": True, "role": role}