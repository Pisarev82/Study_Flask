from enum import Enum

from flask_sqlalchemy import SQLAlchemy

# создаем базу данных
db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    grade  = db.relationship('Grade', backref='student', lazy=True)

    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.group},  {self.email}, {self.grade},"


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade_value = db.Column(db.Integer, nullable=False)
    lesson_title = db.Column(db.String(50), nullable=False)
    # Ссылка на Student
    students = db.Column(db.Integer, db.ForeignKey('student.id'))