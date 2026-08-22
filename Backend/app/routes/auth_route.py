from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)

from app.services.auth_service import (
    authenticate_user,
    register_user,
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)

def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        user = register_user(
            db = db,
            email=request.email,
            password=request.password,
        )
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return{
        "message": "Account created Successfully",
        "user_id": user.id,
        "email": user.email,
    }

@router.post(
    "/login",
    response_model=TokenResponse,
)

def login(
    request:LoginRequest,
    db:Session = Depends(get_db)
):
    token = authenticate_user(
        db = db,
        email = request.email,
        password = request.password,
    )

    if not token:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or passowrd"
        )

    return TokenResponse(
        access_token=token,
    )
