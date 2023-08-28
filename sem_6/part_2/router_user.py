from fastapi import APIRouter
from db import *
from models import InputUser, User

router = APIRouter()


@router.get('/user/{item_id}', response_model=User)
async def get_user(user_id: int):
    query = users_db.select().where(users_db.c.id == user_id)
    return await db.fetch_one(query)

@router.get("/users/", response_model=list[User])
async def read_users():
    query = users_db.select()
    return await db.fetch_all(query)

@router.post('/user/', response_model=int)
async def inp_post(user: InputUser):
    query = users_db.insert().values(
        login=user.login,
        password=user.password,
        email=user.email)
    last_record_id = await db.execute(query)
    return last_record_id


@router.put("/user/replace/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: InputUser):
    query = users_db.update()\
        .where(users_db.c.id == user_id)\
        .values(**new_user.dict())
    await db.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete("/users/del/{user_id}")
async def delete_user(user_id: int):
    query = users_db.delete().where(users_db.c.id == user_id)
    await db.execute(query)
    return {'message': 'User deleted'}