# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.db.postgres import Reminder
from app.models.requests.reminder import ReminderCreate, ReminderRead, ReminderUpdate
from app.api.deps import get_db

router = APIRouter(prefix="/reminder", tags=["reminders"])

@router.post("/create")
def create_reminder(reminder: ReminderCreate, db: Session = Depends(get_db)):
    new_reminder = Reminder(title=reminder.title,
                            user_id=reminder.user_id,
                            frequency=reminder.frequency,
                            time_of_day=reminder.time_of_day,
                            is_active=reminder.is_active)
    db.add(new_reminder)
    db.commit()
    return {"success": True, "message": "Reminder created successfully"}

@router.get("/get/{reminder_id}", response_model=ReminderRead)
def get_reminder(reminder_id: int, db: Session = Depends(get_db)):
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return reminder

@router.put("/update")
def update_reminder(updated_reminder: ReminderUpdate, db: Session = Depends(get_db)):
    current_reminder = db.query(Reminder).filter(Reminder.id == updated_reminder.id).first()
    if not current_reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    for key, value in updated_reminder.model_dump().items():
        if hasattr(current_reminder, key):
            setattr(current_reminder, key, value)
    return {"success": True, "message": "Reminder updated successfully"}

@router.delete("/delete/{reminder_id}")
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    db.delete(reminder)
    db.commit()
    return {"success": True, "message": "Reminder deleted successfully"}


