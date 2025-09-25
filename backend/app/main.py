from fastapi import FastAPI
from app.routers import tasks
from app.database.connection import init_db
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(tasks.router)

@app.get("/")
def root():
    return "Server is running"

@app.get("/swagger", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)