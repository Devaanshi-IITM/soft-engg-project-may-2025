# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.postgres import Reminder
from app.models.request import ReminderCreate, ReminderRead
from app.api.deps import get_db

router = APIRouter(prefix="/reminder", tags=["users"])

@router.post("/create", response_model=ReminderCreate)
def create_reminder(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    return new_user

@router.get("/get/{user_id}", response_model=ReminderRead)
def get_reminder(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/update", response_model=UserRead)
def update_reminder(user: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/delete/{user_id}", response_model=UserRead)
def delete_reminder(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

