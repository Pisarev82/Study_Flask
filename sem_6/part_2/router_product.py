from fastapi import APIRouter
from db import *
from models import InputProduct, Product

router = APIRouter()


@router.get('/product/{item_id}', response_model=Product)
async def get_product(product_db: int):
    query = product_db.select().where(product_db.c.id == product_db)
    return await db.fetch_one(query)

@router.get("/products/", response_model=list[Product])
async def read_product():
    query = product_db.select()
    return await db.fetch_all(query)

@router.post('/product/', response_model=int)
async def inp_product(product: InputProduct):
    query = product_db.insert().values(
        name=product.name,
        description=product.description,
        price=product.price,
    )
    last_record_id = await db.execute(query)
    return last_record_id


@router.put("/product/replace/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: InputProduct):
    query = product_db.update()\
        .where(product_db.c.id == product_id)\
        .values(**new_product.dict())
    await db.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/product/del/{product_id}")
async def delete_product(product_id: int):
    query = product_db.delete().where(product_db.c.id == product_id)
    await db.execute(query)
    return {'message': 'Product deleted'}