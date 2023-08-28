from datetime import datetime
from pydantic import BaseModel, Field


class InputUser(BaseModel):
    login: str = Field(..., title="Login", min_length=4)
    password: str = Field(..., title="Password", min_length=6)
    email: str = Field(..., title="E-mail", min_length=5)


class User(InputUser):
    id: int


class InputProduct(BaseModel):
    name: str = Field(..., title="Product name", min_length=3)
    description: str = Field(..., title="Product description", min_length=3)
    price: float = Field(..., title="Product price", gt=0)


class Product(InputProduct):
    id: int


class InputOrder(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_status: bool = Field(True, title="Order status", gt=0)


class Order(InputOrder):
    id: int
    order_date: datetime
