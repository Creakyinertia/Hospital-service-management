from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from backend.connections.database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = 'patient_info'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String)
    dob = Column(Date)
    contact_number = Column(String)
    email = Column(String, unique=True, index=True)
    aadhar_number = Column(String, index=True)
    address = Column(String)
    emergency_number = Column(String, index=True)
    Nationality = Column(String, index=True)
    Date_of_admission = Column(DateTime, default=datetime.datetime.utcnow)
