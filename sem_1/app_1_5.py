"""Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Николай</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
def index():
    return html


if __name__ == '__main__':
    app.run(debug=True)
