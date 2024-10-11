from fastapi import FastAPI
from sqladmin import ModelView, Admin
from sqlalchemy.ext.asyncio import AsyncEngine

from .dependecies import Driver, Client, Car, Category, Order


class DriverModelView(ModelView, model=Driver):
    column_list = [Driver.name, Driver.experience, Driver.category]
    form_excluded_columns = [Driver.created_at, Driver.updated_at]


class ClientModelView(ModelView, model=Client):
    column_list = [Client.name, Client.rating]
    form_excluded_columns = [Client.created_at, Client.updated_at]


class CarModelView(ModelView, model=Car):
    column_list = [Car.brand, Car.category, Car.category_id, Car.release, Car.condition, Car.configuration]
    form_excluded_columns = [Car.created_at, Car.updated_at]


class CategoryModelView(ModelView, model=Category):
    column_list = [Category.title, Category.schedule]
    form_excluded_columns = [Category.created_at, Category.updated_at]

class OrderModelView(ModelView, model=Order):
    column_list = [Order.price, Order.date_trip, Order.travel_time, Order.client_id, Order.driver_id]
    form_excluded_columns = [Order.created_at, Order.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(DriverModelView)
    admin.add_view(CarModelView)
    admin.add_view(ClientModelView)
    admin.add_view(CategoryModelView)
    admin.add_view(OrderModelView)

