from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.task import Task

router = APIRouter(
    prefix="/tasks"
)

@router.get("/")
def get_tasks():
    return []

@router.post("/")
def create_task(task: Task, db: Session = Depends(get_db)):
    pass