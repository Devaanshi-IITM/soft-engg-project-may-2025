# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.postgres import Reminder
from app.models.request import ReminderCreate, ReminderRead
from app.models.request import UserCreate, UserRead
from app.api.deps import get_db

router = APIRouter(prefix="/content", tags=["content"])

@router.post("/create", response_model=ReminderRead)
def create_content(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    return new_user

@router.get("/get/{content_id}", response_model=ReminderRead)
def get_content(content_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/delete/{content_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

