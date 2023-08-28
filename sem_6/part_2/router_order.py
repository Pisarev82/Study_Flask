import time
from datetime import datetime

from fastapi import APIRouter
from db import *
from models import InputOrder, Order

router = APIRouter()


@router.get('/order/{item_id}', response_model=Order)
async def get_order(order_id: int):
    query = order_db.select().where(order_db.c.id == order_id)
    return await db.fetch_one(query)

@router.get("/orders/", response_model=list[Order])
async def read_orders():
    query = order_db.select()
    return await db.fetch_all(query)

@router.post('/order/', response_model=int)
async def inp_order(order: InputOrder):
    query = order_db.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        order_status=order.order_status,
        order_date=datetime.now(),
    )
    last_record_id = await db.execute(query)
    return last_record_id


@router.put("/order/replace/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: InputOrder):
    query = order_db.update()\
        .where(order_db.c.id == order_id)\
        .values(**new_order.dict())
    await db.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/del/{order_id}")
async def delete_order(order_id: int):
    query = order_db.delete().where(order_db.c.id == order_id)
    await db.execute(query)
    return {'message': 'Order deleted'}