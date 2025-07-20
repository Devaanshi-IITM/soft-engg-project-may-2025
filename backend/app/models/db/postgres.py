import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.db.postgres import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=False)
    gender = Column(String, nullable=True)
    phone_number = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    frequency = Column(String, nullable=False)
    time_of_day = Column(Time, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)



class Content(Base):
    __tablename__ = "contents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content_id = Column(UUID(as_uuid=True), ForeignKey("contents.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User", back_populates="preferences")
    content = relationship("Content", back_populates="preferences")


class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    recipient_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime, default=datetime.now())
