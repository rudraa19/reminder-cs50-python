from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from app.models.task import Base

engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    try: 
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)