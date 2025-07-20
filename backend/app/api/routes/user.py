# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.db.postgres import User
from app.models.requests.user import UserCreate, UserUpdate, UserRead
from app.api.deps import get_db

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/create")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, 
                    email=user.email, 
                    age=user.age, 
                    gender=user.gender, 
                    phone_number=user.phone_number, 
                    is_admin=user.is_admin)
    
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.phone_number == user.phone_number).first():
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    db.add(new_user)
    db.commit()
    return {"success": True, "message": "User created successfully"}

@router.get("/get/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/update")
def update_user(updated_user: UserUpdate, db: Session = Depends(get_db)):
    current_user = db.query(User).filter(User.id == updated_user.id).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in updated_user.model_dump().items():
        if hasattr(current_user, key):
            setattr(current_user, key, value)

    db.commit()
    return {"success": True, "message": "User updated successfully"}

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"success": True, "message": "User deleted successfully"}
