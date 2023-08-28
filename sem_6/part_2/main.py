from fastapi import FastAPI
from db import *
import router_user, router_product, router_order


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router_user.router, tags=['users'])
app.include_router(router_product.router, tags=['products'])
app.include_router(router_order.router, tags=['orders'])

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
