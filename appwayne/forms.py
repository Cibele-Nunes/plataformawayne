from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Length

class RegistrationForm(FlaskForm):
    nome = StringField('Digite o seu nome', validators=[InputRequired(), Length(min=3, max=50)])
    sobrenome = StringField('Seu sobrenome', validators=[InputRequired(), Length(min=3, max=50)])
    user_nome = StringField('Crie o seu nome de usuário', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!'), InputRequired(), Length(min=4, max=50)])
    senha = PasswordField('Crie a sua senha', validators=[InputRequired(), EqualTo('confirm_senha', message='As senhas devem ser iguais'), Length(min=6, max=50)])
    confirm_senha = PasswordField('Confirme a sua senha', validators=[InputRequired(), Length(min=6, max=50)])
    newsletter = BooleanField('Marque, se dseja receber nossas newsletters.')
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    user_nome = StringField('Nome de usuário', validators=[InputRequired(message='Usuário não cadastrado!'), Length(min=4, max=50)])
    senha = PasswordField('Senha', validators=[InputRequired(), Length(min=6, max=50)])
    lembre_me = BooleanField('Marque, para continuar conectado.')
    nova_senha = SubmitField('Esqueceu sua senha?')
    botao = SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!'), InputRequired(message='Digite seu e-mail.'), Length(min=4, max=50)])
    submit = SubmitField('Enviar')