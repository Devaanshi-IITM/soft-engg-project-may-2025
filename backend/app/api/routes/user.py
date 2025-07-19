# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.postgres import User
from app.models.request import UserCreate, UserRead
from app.api.deps import get_db

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/create", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    return new_user

@router.get("/get/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/update", response_model=UserRead)
def update_user(updated_user: UserUpdate, db: Session = Depends(get_db)):
    current_user = db.query(User).filter(User.id == updated_user.id).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(current_user)
    db.add(updated_user)
    db.commit()
    return updated_user

@router.delete("/delete/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user
