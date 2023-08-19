from enum import Enum

from flask_sqlalchemy import SQLAlchemy

# создаем базу данных
db = SQLAlchemy()


class GenderEnum(Enum):
    male = 'male'
    female = 'female'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    group = db.Column(db.String(50), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, {self.age}, {self.group},  {self.faculty_id}"


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # Ссылка на Student
    students = db.relationship('Student', backref='faculty', lazy=True)