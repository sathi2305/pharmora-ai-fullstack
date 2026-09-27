from sqlalchemy import Column, String, Integer, Float, DateTime, JSON, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
import uuid, datetime
Base=declarative_base()
class User(Base):
    __tablename__="users"
    id=Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email=Column(String, unique=True, index=True)
    password_hash=Column(String)
    full_name=Column(String)
    age=Column(Integer)
    gender=Column(String)
    preferred_language=Column(String, default="en")
    health_profile=Column(JSON, default=dict)
    is_google=Column(Boolean, default=False)
    created_at=Column(DateTime, default=datetime.datetime.utcnow)
class Medicine(Base):
    __tablename__="medicines"
    id=Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    brand_name=Column(String, index=True)
    generic_name=Column(String, index=True)
    composition=Column(JSON)
    manufacturer=Column(String)
    mrp=Column(Float)
    atc_code=Column(String)
    description=Column(Text)
