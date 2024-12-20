from fastapi import FastAPI
from backend.routes.api import router as api_route




app = FastAPI(title="Hospital management system",)


app.include_router(api_route)