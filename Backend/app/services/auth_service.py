from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password
)

from app.db.models import User

def register_user(
    db:Session,
    email:str,
    password:str,
) -> User:

    existing_user = db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user:
        raise ValueError("Email is already registered")

    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(
    db: Session,
    email:str,
    password:str
) ->str | None :

    user = db.scalar(
        select(User).where(User.email == email)
    )

    if not user:
        return None
        
    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return create_access_token(user.id)
    

