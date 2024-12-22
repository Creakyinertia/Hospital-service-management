from fastapi import FastAPI
from backend.routes.api import router as api_route
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Hospital management system",)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


app.include_router(api_route)