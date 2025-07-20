# app/schemas/message.py

from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class MessageBase(BaseModel):
    sender_id: UUID
    recipient_id: UUID

class MessageCreate(MessageBase):
    content: str

class MessageRead(MessageBase):
    id: UUID
    timestamp: datetime
