from fastapi import FastAPI
from sqladmin import ModelView, Admin
from sqlalchemy.ext.asyncio import AsyncEngine
from .dependecies import Driver

class DriverModelView(ModelView, model=Driver):
    column_list = [Driver.name, Driver.experience, Driver.category]
    form_excluded_columns = [Driver.created_at, Driver.updated_at]



def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(DriverModelView)

