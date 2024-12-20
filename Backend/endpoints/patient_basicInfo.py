from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.orm_classes import basic_info_models
from backend.base_models import basic_info_schemas
from backend.commons import basic_Info
from backend.connections.database import SessionLocal,engine,get_db


basic_info_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/create-patient-record/")
def create_patient(user: basic_info_schemas.User, db: Session = Depends(get_db)):
    return basic_Info.create_user(db=db, user=user)

