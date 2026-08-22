from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement = True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique = True,
        nullable = False,
    )

    password_hashed: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default = datetime.utcnow,
        nullable = False,
    )

    profile = relationship(
        "UserProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

class UserProfile(Base):
    __tablename__ = "user_profiles"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    age: Mapped[int] = mapped_column(
        nullable=True,
    )

    sex: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )
    
    height_cm: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    weight_kg: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    activity_level: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    goal: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    target_weight_kg: Mapped[float | None] = mapped_column(
        nullable=True,  
    )

    daily_budget: Mapped[float | None] = mapped_column(
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="profile",
    )