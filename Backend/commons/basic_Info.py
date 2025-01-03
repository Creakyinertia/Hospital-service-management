from sqlalchemy.orm import Session
from backend.base_models import basic_info_schemas
from backend.orm_classes import basic_info_models
from backend.orm_classes.basic_info_models import User
# from backend.base_models.basic_info_schemas import UserBase
from backend.commons.response import success_message,error_message
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, Depends,status,HTTPException
from fastapi import FastAPI, Response, status
from starlette.responses import JSONResponse
from uuid import UUID
import uuid




# Check if details already exists in the database
def get_current_details(db: Session,user: basic_info_schemas.User):
    request_email=user.email
    email_exist = db.query(basic_info_models.User).filter(basic_info_models.User.email == request_email).first()
    if email_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "message": error_message['102'],
                "statusCode": 409,
                "errorCode": "409-A",
            }
        ) 
    else:
        return None
    
    


#create Patient details 
def create_user(db: Session, user: basic_info_schemas.User):
    if get_current_details(db, user):
        return get_current_details(db, user)
    
    else:
        username = str(user.first_name)+"_"+ str(user.last_name)
        db_item = basic_info_models.User(
            username=username,
            gender=user.gender,
            dob=user.dob,
            contact_number=user.contact_number,
            email=user.email,
            aadhar_number=user.aadhar_number,
            address=user.address,
            emergency_number=user.emergency_number,
            Nationality=user.Nationality,
            Date_of_admission=user.Date_of_admission,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return {
            "detail": {
                "message": success_message['100'],
                "data": [db_item],
                "statusCode": 200,
                "errorCode": None,
            }
        }
    

#get Patient details with username and contact
def get_patient_records(username:str,contact:str,db: Session):
    request_contact=contact
    request_username=username
    patient_details = db.query(basic_info_models.User).filter(
        basic_info_models.User.contact_number == request_contact,
        basic_info_models.User.username == request_username
        ).all()
    if patient_details:
        return {
            "detail": {
                "message": success_message['105']%request_username,
                "data": [patient_details],
                "statusCode": 200,
                "errorCode": None,
            }
        }
    

        
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message":error_message['101']%request_username,
                "statusCode": 404,
                "errorCode": None,
            }
        )



# Delete patient records
def remove_patient_records(username: str, contact: str, db: Session):
    request_contact = contact
    request_username = username
    patient_details = db.query(basic_info_models.User).filter(
        basic_info_models.User.contact_number == request_contact,
        basic_info_models.User.username == request_username
    ).first()
    
    if patient_details:
        db.delete(patient_details)
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail={
                "message": success_message['106'] % request_username,
                "statusCode": 404,
                "errorCode": None,
            }
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": error_message['101'] % request_username,
                "statusCode": 404,
                "errorCode": None,
            }
        )




def is_valid_uuid(value):
    try:
        UUID(value) 
        return True
    except ValueError:
        return False



# update patient records
def update_patient_records(id:str,user: basic_info_schemas.User, db: Session):
    unique_id = id
    request_username = str(user.first_name)+"_"+ str(user.last_name)
    if is_valid_uuid(unique_id):
        # all_ids = [str(id[0]) for id in db.query(basic_info_models.User.id).all()]
        if str(unique_id) == str(UUID(unique_id)):
            patient_details = db.query(basic_info_models.User).filter(basic_info_models.User.id == unique_id).first()
            # patient_details.username = request_username
            patient_details.gender = user.gender
            patient_details.dob = user.dob
            patient_details.contact_number = user.contact_number
            patient_details.email = user.email
            patient_details.emergency_number =  user.emergency_number
            patient_details.address = user.address
            patient_details.emergency_number = user.emergency_number
            patient_details.aadhar_number = user.aadhar_number
            patient_details.Nationality = user.Nationality
            patient_details.Date_of_admission = user.Date_of_admission
        
            db.commit()
        
            return {
                "detail": {
                "message": success_message['107'] % unique_id,
                "statusCode": 200,
                "errorCode": None,
                }
            }
        else:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail={
                        "message": error_message['105'] % unique_id,
                        "statusCode": 404,
                        "errorCode": None,
                    }
                )
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": error_message['105'] % unique_id,
                    "statusCode": 404,
                    "errorCode": None,
                }
            )
    