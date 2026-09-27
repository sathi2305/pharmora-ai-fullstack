from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..core.security import get_password_hash, verify_password, create_access_token
router=APIRouter()
USERS_DB={}
class SignupRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    age: int=25
    gender: str="other"
    language: str="en"
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
@router.post("/signup")
def signup(req: SignupRequest):
    if req.email in USERS_DB: raise HTTPException(400, "Exists")
    user={"id": f"user_{len(USERS_DB)+1}", "email": req.email, "full_name": req.full_name, "preferred_language": req.language, "health_profile": {"genotype": {"CYP2C9": "*1/*1"}}}
    USERS_DB[req.email]={"user": user, "hash": get_password_hash(req.password)}
    token=create_access_token({"sub": req.email})
    return {"success": True, "data": {"access_token": token, "user": user}}
@router.post("/login")
def login(req: LoginRequest):
    rec=USERS_DB.get(req.email)
    if not rec or not verify_password(req.password, rec["hash"]): raise HTTPException(401, "Invalid")
    token=create_access_token({"sub": req.email})
    return {"success": True, "data": {"access_token": token, "user": rec["user"]}}
@router.post("/google")
def google_login(id_token: str):
    user={"id": "google_123", "email": "googleuser@test.com", "full_name": "Google User", "preferred_language": "en"}
    token=create_access_token({"sub": user["email"]})
    return {"success": True, "data": {"access_token": token, "user": user}}
