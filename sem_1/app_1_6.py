"""Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст"""
from flask import Flask, render_template

app = Flask(__name__)


_students = [
    {"firstname": "Nikolay", "lastname": "Pisarev", "age": 41, "rate": 5},
    {"firstname": "Nikolay", "lastname": "Pisarev", "age": 41, "rate": 5},
    {"firstname": "Nikolay", "lastname": "Pisarev", "age": 41, "rate": 5}
    ]


@app.route('/students/')
def students():
    context = {'students': _students}
    return render_template("students.html", students=_students)
    # return render_template("students.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
