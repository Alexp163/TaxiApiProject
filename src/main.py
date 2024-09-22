from fastapi import FastAPI

from admin.panel import register_admin
from database import engine
from driver.router import router as driver_router

app = FastAPI()
app.include_router(driver_router)


register_admin(app, engine)
