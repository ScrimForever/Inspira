from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from inspira.backend.core.config import DB_NAME

SQLITE = f'sqlite:///{DB_NAME}'
engine = create_engine(SQLITE)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()