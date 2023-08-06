"""Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    return render_template("news.html", )

@app.route('/about/')
def news():
    return render_template("news.html", )

@app.route('/')
def news():
    return render_template("news.html", )


if __name__ == '__main__':
    app.run(debug=True)