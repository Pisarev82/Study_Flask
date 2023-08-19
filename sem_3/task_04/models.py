from enum import Enum

from flask_sqlalchemy import SQLAlchemy

# создаем базу данных
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.email}, {self.password},"

