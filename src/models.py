import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi_restful.session import FastAPISessionMaker

load_dotenv(".env")

engine = create_engine(os.getenv('DB_CONNECT'), pool_size=5, max_overflow=-1)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

class BaseModel(Base):
    __abstract__ = True

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
UtilsFastapiConnectDB = FastAPISessionMaker(os.getenv('DB_CONNECT'))