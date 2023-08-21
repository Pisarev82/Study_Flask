"""
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: bool


class Task(TaskIn):
    id: int


# tasks = [{'id': 1,
#           'title': 'Задача 1',
#           'description': 'Описание 1-й задачи',
#           'status': True}]

tasks = []


@app.post("/items")
async def create_item(item: TaskIn):
    print(item)
    task = Task
    task.id = len(tasks)
    task.status = item.status
    task.title = item.title
    task.description = item.description
    tasks.append(task)


@app.get("/", response_model=list[Task])
async def read_root():
    return tasks


@app.get("/task/{id}", response_model=Task)
async def get_task_by_id_root(id: int):
    for task in tasks:
        if task.id == id:
            return task


@app.put("/items/{item_id}")
async def update_item(item_id: int, new_task: TaskIn):
    for task in tasks:
        if task.id == item_id:
            task.status = new_task.status
            task.title = new_task.title
            task.description = new_task.description
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/del/{item_id}")
async def del_item(item_id: int):
    for task in tasks:
        if task.id == item_id:
            tasks.remove(task)
            return tasks
    raise HTTPException(status_code=404, detail="Task not found")


# if __name__ == '__main__':
#     uvicorn.run(
#         "task_5_1:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True
#         )