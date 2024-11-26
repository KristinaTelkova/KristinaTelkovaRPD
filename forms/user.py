from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль',validators=[DataRequired()])
    name = StringField('Имя пользователя',validators=[DataRequired()])
    submit = SubmitField('Войти')