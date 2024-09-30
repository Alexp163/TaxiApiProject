from fastapi import FastAPI

from admin.panel import register_admin
from database import engine
from driver.router import router as driver_router
from client.router import router as client_router
from car.router import router as car_router

app = FastAPI()
app.include_router(driver_router)
app.include_router(client_router)
app.include_router(car_router)


register_admin(app, engine)
