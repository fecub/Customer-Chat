from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database.session import get_db
from core.models.user import User
from core.schema import user_schema

auth_router = APIRouter()


@auth_router.post("/users/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@auth_router.post("/users/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
