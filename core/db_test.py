
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Database session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False
)


# Base class for database models
class Base(DeclarativeBase):
    pass


# Create database tables
Base.metadata.create_all(bind=engine)
