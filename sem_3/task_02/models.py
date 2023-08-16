from flask_sqlalchemy import SQLAlchemy

# создаем базу данных
db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    authors = db.relationship('Author', secondary='book_author',
                              backref='books', lazy=True)

    def __repr__(self):
        return f"{self.name}"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))