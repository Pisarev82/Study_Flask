"""Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке

Задание №8
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.
"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from task_04.models import db, User
from task_04.forms import RegisterForm, LoginForm
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_task_04.db'
app.config['SECRET_KEY'] = 'SECRET'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init_db")
def init_db():
    db.create_all()


@app.route("/")
def index():
    return "<H1>Hi!4</H1>"


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        ex_user = User.query.filter((User.name == name) | (User.email == email)).first()
        if ex_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            form.email.errors.append(error_msg)
            return render_template('register.html', form=form)
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return "register success"
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
