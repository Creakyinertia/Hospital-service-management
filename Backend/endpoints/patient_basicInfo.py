from fastapi import FastAPI, Depends,status,HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.orm_classes import basic_info_models
from backend.base_models import basic_info_schemas
from backend.commons import basic_Info
from backend.connections.database import SessionLocal,engine,get_db
from fastapi import FastAPI, Response, status


basic_info_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/create-patient-record/",status_code=status.HTTP_201_CREATED,tags=["Patient Records"])
async def create_patient(user: basic_info_schemas.User, db: Session = Depends(get_db)):
    basic_Info.get_current_details(db=db, user=user)
    return basic_Info.create_user(db=db, user=user)

@router.get("/patient-record-details/",tags=["Patient Records"])
async def create_patient(username:str,contact:str, db: Session = Depends(get_db)):
    basic_Info.get_patient_records(username =username ,db=db, contact=contact)
    return basic_Info.get_patient_records(username =username ,db=db, contact=contact)
