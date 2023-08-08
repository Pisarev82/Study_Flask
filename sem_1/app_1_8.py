"""Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template("main.html", **context)

@app.route('/about/')
def news():
    context = {'title': 'База статей'}
    return render_template("clothes.html", )



if __name__ == '__main__':
    app.run(debug=True)