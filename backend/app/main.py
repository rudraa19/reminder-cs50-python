from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.task import Task as TaskModel
from app.routers import tasks
from app.database.connection import get_db, init_db
from scalar_fastapi import get_scalar_api_reference
from datetime import date
from app.config import NTFY_ID
import requests

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(tasks.router)

@app.get("/")
def root():
    return "Server is running"

@app.get("/cj")
def cron_job(db : Session = Depends(get_db)):
    date_today = date.today()
    due_tasks = db.query(TaskModel).filter(TaskModel.due_date == date_today, TaskModel.is_completed == False).all()

    for task in due_tasks:
        try:
            headers = {
                "Title": task.title
            }
            data = task.desc
            requests.post(f"https://ntfy.sh/{NTFY_ID}", headers=headers, data=data)
        except requests.exceptions.RequestException as e:
            print("Failed to notify: {e}")
    
    return "All notifications sent!"

@app.get("/swagger", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)