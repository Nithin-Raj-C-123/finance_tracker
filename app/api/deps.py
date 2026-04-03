from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

# DB SESSION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MOCK USER (change role here to test)
def get_current_user():
    return {"id": 1, "role": "admin"}
    # change role to:
    # "viewer"
    # "analyst"
    # "admin"

# ROLE CHECK FUNCTION
def require_role(required_role: str):
    def role_checker(user=Depends(get_current_user)):
        roles = ["viewer", "analyst", "admin"]

        if roles.index(user["role"]) < roles.index(required_role):
            raise HTTPException(status_code=403, detail="Not enough permissions")

        return user

    return role_checker