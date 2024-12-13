from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    nome = StringField('Digite o seu nome', validators=[DataRequired(), Length(min=3, max=50)])
    sobrenome = StringField('Seu sobrenome', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!'), DataRequired(), Length(min=4, max=50)])
    telefone = IntegerField('Número do telefone', validators=[Length(min=10, max=20)])
    senha = PasswordField('Crie uma senha', validators=[InputRequired(), EqualTo('confirm_senha', message='As senhas devem ser iguais'), Length(min=6, max=50)])
    confirm_senha = PasswordField('Confirme a sua senha', validators=[InputRequired(), Length(min=6, max=50)])
    botao = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Seu e-mail cadastrado', validators=[InputRequired(), Email(message='E-mail não cadastrado!'), Length(min=4, max=50)])
    senha = PasswordField('Senha', validators=[InputRequired(), Length(min=6, max=50)])
    botao = SubmitField('Login')