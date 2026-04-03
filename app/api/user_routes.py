from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.crud.user_crud import create_user
from app.api.deps import get_db

router = APIRouter(prefix="/users")

@router.post("/")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.role)