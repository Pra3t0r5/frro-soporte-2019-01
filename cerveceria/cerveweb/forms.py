from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistroUsuarioForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[
                           DataRequired(),
                           Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirmar Password', validators=[
                                     DataRequired(),
                                     EqualTo('password')])
    submit = SubmitField('Registrame')