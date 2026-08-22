from fastapi import FastAPI
from app.db.database import engine, Base
from app.db import models
from app.routes.test_route import router as test_router
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth_route import router as auth_router


app = FastAPI(
    title="DeficitWise API",
    description="Calorie deficit and budget-aware meal planning API",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(test_router)

@app.get("/")
def root():
    return {
        "message": "DeficitWise API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }