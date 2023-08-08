"""Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""
from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)

headers = ("title", "description", "date")
News = namedtuple('News', headers)


@app.route('/news/')
def news():
    news_list = [News("Новость 1", "Очень интересная новость", '30.07.2023'),
                 News("Новость 2", "Не Очень интересная новость", '30.07.2023'),
                 News("Новость 3", "Очень-очень интересная новость", '30.07.2023')]
    return render_template("news.html", news=news_list)


if __name__ == '__main__':
    app.run(debug=True)
