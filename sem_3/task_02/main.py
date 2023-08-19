# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.
from flask import Flask, render_template

from sem_3.task_02.models import db, Book, Author, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.route("/")
def index():
    return "<H1>Hi2</H1>"


@app.cli.command("init_db")
def init_db():
    db.create_all()


@app.route("/books/")
def get_books():
    all_books = Book.query.all()
    return render_template("books.html", all_books=all_books)


if __name__ == '__main__':
    app.run(debug=True)