from pydantic import BaseModel
from typing import Optional
from datetime import date

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    desc: str
    due_date: date
    is_completed: bool = False

    class Config:
        orm_mode = True
