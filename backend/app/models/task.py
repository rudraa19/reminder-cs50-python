from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):

    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=True)
    due_date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)   