from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

class AddReminderInput(BaseModel):
    reason: str          
    date  : str         
    time: Optional[str]

class UserInput(BaseModel):
    text: str

class AIResponse(BaseModel):
    response: str
    reminders_list: Optional[List[dict]] = None


