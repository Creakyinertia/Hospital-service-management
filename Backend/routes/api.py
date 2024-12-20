from fastapi import APIRouter
from backend.endpoints import patient_basicInfo


router = APIRouter()

router.include_router(patient_basicInfo.router)


