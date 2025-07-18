from sqlalchemy import Column, Integer, String
from .database import Base

class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True, index=True)
    senior_name = Column(String)
    senior_email = Column(String, unique=True, index=True)
    senior_dob = Column(String)
    senior_gender = Column(String)
    senior_mobile = Column(String, nullable=True)
    child_name = Column(String)
    child_email = Column(String, unique=True, index=True)
    child_mobile = Column(String, nullable=True)
    role = Column(String, default='guardian')
