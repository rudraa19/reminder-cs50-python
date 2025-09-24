from fastapi import FastAPI
from .routers import tasks
from database.connection import session

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def root():
    return "Server is running"