from fastapi import FastAPI
from app.routers import tasks
from app.database.connection import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(tasks.router)

@app.get("/")
def root():
    return "Server is running"