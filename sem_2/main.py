# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/hello/')
def task_1():
    # Создать страницу, на которой будет кнопка "Нажми меня", при
    # нажатии на которую будет переход на другую страницу с
    # приветствием пользователя по имени.
    return 'Привет Николай'


@app.route("/task_2")
def task_2():
    # Создать страницу, на которой будет изображение и ссылка
    # на другую страницу, на которой будет отображаться форма
    # для загрузки изображений.
    if request.method == 'GET':
        return render_template("task_2.html")
    file = request.files.get('file')
    file_name = 'img/' + secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.cwd(), 'static', file_name))
    return render_template("task_2.html", file_name=file_name)




if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
