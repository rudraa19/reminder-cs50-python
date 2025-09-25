from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.task import Task as TaskModel  # SQLAlchemy model
from app.schemas.task import Task as TaskSchema  # Pydantic schema

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/", response_model=list[TaskSchema])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return tasks

@router.post("/", response_model=TaskSchema)
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    db_task = TaskModel(
        title=task.title,
        desc=task.desc,
        due_date=task.due_date,
        is_completed=task.is_completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, updated_task: TaskSchema, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = updated_task.title
    task.desc = updated_task.desc
    task.due_date = updated_task.due_date
    task.is_completed = updated_task.is_completed

    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
