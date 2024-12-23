from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from backend.connections.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class User(Base):
    __tablename__ = 'patient_info'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) 
    username = Column(String, index=True)
    gender = Column(String)
    dob = Column(Date)
    contact_number = Column(String)
    email = Column(String, unique=True, index=True)
    aadhar_number = Column(String, index=True)
    address = Column(String)
    emergency_number = Column(String, index=True)
    Nationality = Column(String, index=True)
    Date_of_admission = Column(DateTime, default=datetime.datetime.utcnow)
