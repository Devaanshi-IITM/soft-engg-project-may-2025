from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, time
from typing import Optional

class ReminderBase(BaseModel):
    title: str
    frequency: str
    time_of_day: time
    is_active: bool = True

class ReminderCreate(ReminderBase):
    user_id: UUID

class ReminderUpdate(ReminderBase):
    id: UUID

class ReminderRead(ReminderBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True

