from pydantic import BaseModel, EmailStr, validator, Field, conint
from datetime import date
import re
from typing import Literal

class User(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    gender: Literal['female', 'male']
    dob: date
    contact_number: str = Field(..., min_length=10, max_length=10)
    email: str
    aadhar_number:str=Field(..., min_length=10, max_length=10)
    address: str = Field(..., min_length=5)
    emergency_number:str = Field(..., min_length=10, max_length=10)
    Nationality:str=Field(..., min_length=10, max_length=10)
    Date_of_admission:date



