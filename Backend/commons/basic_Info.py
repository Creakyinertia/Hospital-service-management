from sqlalchemy.orm import Session
from backend.base_models import basic_info_schemas
from backend.orm_classes import basic_info_models
# from backend.base_models.basic_info_schemas import UserBase





def create_user(db: Session, user: basic_info_schemas.User):
    db_item = basic_info_models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        dob=user.dob,
        contact_number=user.contact_number,
        email=user.email,
        aadhar_number=user.aadhar_number,
        address=user.address,
        emergency_number = user.emergency_number,
        Nationality = user.Nationality,
        Date_of_admission = user.Date_of_admission
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



