# app/models/message_model.py
from pydantic import BaseModel, UUID4

class Message(BaseModel):
    message_id: UUID4
    content: str