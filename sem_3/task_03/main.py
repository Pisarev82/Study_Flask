"""Доработаем задача про студентов
Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
База данных должна содержать две таблицы: "Студенты" и "Оценки".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
Необходимо создать связь между таблицами "Студенты" и "Оценки".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""
from random import choice
from string import ascii_lowercase

from flask import Flask, render_template
from task_03.models import db, Student, Faculty, GenderEnum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_task_03.db'
db.init_app(app)


@app.cli.command("init_db")
def init_db():
    db.create_all()


@app.cli.command("add_student")
def add_student():
    for i in range(1, 6):
        faculty = Faculty(name=f"VIP-{i}")
        db.session.add(faculty)

    db.session.commit()

    for _ in range(1, 21):
        student = Student(first_name=''.join(choice(ascii_lowercase) for _ in range(5)),
                          last_name=''.join(choice(ascii_lowercase) for _ in range(5)),
                          age=choice(range(18, 25)),

                          group=''.join(choice(ascii_lowercase) for _ in range(3)),
                          faculty_id=int(choice(range(1, 6))))
        print(student)
        db.session.add(student)
    db.session.commit()


@app.route("/students/")
def students():
    all_students = Student.query.all()
    print(type(all_students))
    # return "<H1>students!</H1>"
    return render_template("students.html", all_students=all_students)


@app.route("/")
def index():
    return "<H1>Hi!</H1>"


if __name__ == '__main__':
    app.run(debug=True)
