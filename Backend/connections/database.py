from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@172.28.50.172:5432/doctor"  # Change this to your preferred DB URI

engine = create_engine(DATABASE_URL,
    pool_size=10, 
    max_overflow=20,  
    pool_timeout=30,  
    pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()