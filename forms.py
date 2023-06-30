from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(min=2, max=10)])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])

    registrar = SubmitField('Registrar') 


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    senha = PasswordField('Senha', validators=[DataRequired()])
    
    lembrar = BooleanField('Lembrar')
    
    login = SubmitField('Login')