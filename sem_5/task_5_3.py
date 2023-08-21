"""
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.

Задание №4
Создайте маршрут для обновления информации о пользователе (метод PUT).

Задание №5
Создайте маршрут для удаления информации о пользователе (метод DELETE).

Задание №6
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""
import pydantic
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class UserIn(BaseModel):
    name: str
    email: pydantic.EmailStr
    password: str


class User(UserIn):
    id: int


users = []


@app.post("/items", response_model=list[User])
async def create_user(item: UserIn):
    user = User
    user.id = len(users) + 1
    user.name = item.name
    user.email = item.email
    user.password = item.password
    users.append(user)
    return users


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if len(users):
        name = users[0].name
    else:
        name = 'Не найдено'
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "name": name})


@app.put("/items/{item_id}", response_model=list[User])
async def update_item(item_id: int, new_user: UserIn):
    for user in users:
        if user.id == item_id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return users
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/del/{item_id}")
async def delete_item(item_id: int):
    for user in users:
        if user.id == item_id:
            users.remove(user)
            return users
    raise HTTPException(status_code=404, detail="Task not found")
