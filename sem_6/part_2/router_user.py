from fastapi import APIRouter
from db import *
from models import User as model_User
from models import InputUser
from sqlalchemy.orm import Session


router = APIRouter()
db =


@router.get('/user/{item_id}', response_model=model_User)
async def get_user(user_id: int):
    query = User.select().where(User.c.id == user_id)
    user = await database.fetch_one(query)
    return user


@router.post('/user/', response_model=list[model_User])
async def inp_post(user: InputUser):
    new_user = User(
        login=user.login,
        password=user.password,
        email=user.email,
    )
    query = User.insert().values(
        login=user.login,
        password=user.password,
        email=user.email,
    )
    last_record_id = await database.execute(query)
    return {**user, "id": last_record_id}
