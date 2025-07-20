from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ContentBase(BaseModel):
    title: str
    type: str
    file_url: str

class ContentCreate(ContentBase):
    pass

class ContentRead(ContentBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
