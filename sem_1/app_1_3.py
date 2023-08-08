"""Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/<int:nam_a>/<int:nam_b>/')
def sum_(nam_a, nam_b):
    return f'{nam_a} + {nam_b} = {nam_a + nam_b}'


if __name__ == '__main__':
    app.run()
