# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path

from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

users = {"Kolya": "123",
         "admin": "1234"}


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/hello/')
def task_1():
    # Создать страницу, на которой будет кнопка "Нажми меня", при
    # нажатии на которую будет переход на другую страницу с
    # приветствием пользователя по имени.
    return 'Привет Николай'


@app.route("/task_2", methods=['GET', 'POST'])
def task_2():
    # Создать страницу, на которой будет изображение и ссылка
    # на другую страницу, на которой будет отображаться форма
    # для загрузки изображений.
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = 'img/' + secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static', file_name))
        return render_template("task_2.html", file_name=file_name)
    return render_template("task_2.html")


@app.route('/task_3/', methods=['GET', 'POST'])
def task_3():
    # Создать страницу, на которой будет форма для ввода логина и пароля
    # При нажатии на кнопку "Отправить" будет произведена
    # проверка соответствия логина и пароля и переход на
    # страницу приветствия пользователя или страницу с
    # ошибкой.
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login in users.keys() and password == users[login]:
            # Предложенный на семинаре вариант не рабочий не использовать!!!
            # if (login, password) in users.items():
            return f"Hello {login}"
        return "Не правильный логин или пароль"
    return render_template("task_3.html")


@app.route('/task_4/', methods=['GET', 'POST'])
def task_4():
    # Создать страницу, на которой будет форма для ввода текста и
    # кнопка "Отправить"
    # При нажатии кнопки будет произведен подсчет количества слов
    # в тексте и переход на страницу с результатом.
    if request.method == 'POST':
        text = request.form.get('text')
        return str(f'В тексте: \n {escape(text)} {len(text.split(" "))} слов')
    return render_template("task_4.html")


@app.route('/task_5/', methods=['GET', 'POST'])
def task_5():
    # Создать страницу, на которой будет форма для ввода двух
    # чисел и выбор операции (сложение, вычитание, умножение
    # или деление) и кнопка "Вычислить"
    # При нажатии на кнопку будет произведено вычисление
    # результата выбранной операции и переход на страницу с
    # результатом.
    if request.method == 'POST':
        num_1 = request.form.get('num_1')
        num_2 = request.form.get('num_2')
        if request.form.get('+'):
            math_oper = "+"
            res = str(float(num_1) + float(num_2))
        if request.form.get('-'):
            res = str(float(num_1) - float(num_2))
            math_oper = "-"
            return math_oper
        else:
            res = "fack"
            math_oper = "fack"
            return str(f'{escape(num_1)} {math_oper} {num_1} = {res}')
        return math_oper
    return render_template("task_5.html")



if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
