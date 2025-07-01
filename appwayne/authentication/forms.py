from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TelField, IntegerField, FloatField, TextAreaField, SelectField, SelectMultipleField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Length

class RegistrationForm(FlaskForm): 
    nome_completo = StringField('Nome Completo', validators=[InputRequired(), Length(min=3, max=50)])
    nome_social = StringField('Nome Social', validators=[InputRequired()])
    ident_genero = SelectField('Identidade de Gênero', validators=[DataRequired()], choices=[('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Não Binário'), ('4', 'Prefiro não responder')], coerce=str, option_widget=None, validate_choice=True)
    user_nome = StringField('Nome de Usuário', validators=[InputRequired(), Length(min=3, max=50)])
    email = EmailField('E-mail', validators=[Email(message='E-mail inválido!'), InputRequired(), Length(min=4, max=50)])
    celular = TelField('Número do Celular', validators=[InputRequired()])
    num_whatsapp = TelField('Número de Whatsapp', validators=[InputRequired()])
    data_nasc = DateField('Data de Nascimento', validators=[InputRequired()], format='%d-%m-%Y')
    est_civil = SelectField('Estado Civil Oficial', validators=[DataRequired()], choices=[('1', 'Solteiro(a)'), ('2', 'Casado(a)'), ('3', 'Divorciado(a)'), ('4', 'Viúvo(a)')], coerce=str, option_widget=None, validate_choice=True)
    filhos = BooleanField('Filhos?', default=False, validators=[DataRequired()])
    num_filhos = IntegerField('Filhos', validators=[InputRequired(), Length(min=3, max=50)])
    formacao = StringField('Formação', validators=[InputRequired(), Length(min=3, max=50)])
    cep = IntegerField('CEP', validators=[InputRequired()])
    rua = StringField('Rua', validators=[InputRequired(), Length(min=3, max=50)])
    n = IntegerField('N°', validators=[InputRequired(), Length(min=3, max=4)])
    bairro = StringField('Bairro', validators=[InputRequired(), Length(min=3, max=50)])
    cidade = StringField('Cidade', validators=[InputRequired(), Length(min=3, max=50)])
    estado = StringField('Estado', validators=[InputRequired(), Length(min=3, max=50)])
    data_admissao = DateField('Data de Nascimento', validators=[InputRequired()], format='%d-%m-%Y')
    cpf = IntegerField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    rg = IntegerField('RG', validators=[InputRequired()])
    cart_trab = IntegerField('Nº Carteira de Trabalho', validators=[InputRequired()])
    pis = IntegerField('PIS', validators=[InputRequired(), Length(min=3, max=50)])
    salario = FloatField('Salário Inicial', validators=[InputRequired()])
    funcao = SelectField('Função', validators=[DataRequired()], choices=[], coerce=int)
    permissoes = SelectMultipleField('Permissões', validators=[DataRequired()], choices=[], coerce=int)
    jornada = StringField('Jornada de Trabalho', validators=[InputRequired(), Length(min=3, max=50)])
    observacoes = TextAreaField('Informações Complementares', validators=[Length(max=1000)])
    senha = PasswordField('Crie a sua senha', validators=[InputRequired(), EqualTo('confirm_senha', message='As senhas devem ser iguais'), Length(min=6, max=50)])
    confirm_senha = PasswordField('Confirme a sua senha', validators=[InputRequired(), Length(min=6, max=50)])

class LoginForm(FlaskForm):
    user_nome = StringField('Nome de usuário', validators=[InputRequired(message='Usuário não cadastrado!'), Length(min=4, max=50)])
    senha = PasswordField('Senha', validators=[InputRequired(), Length(min=6, max=50)])
    lembre_me = BooleanField('Marque, para continuar conectado.')
    nova_senha = SubmitField('Esqueceu sua senha?')
    botao = SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!'), InputRequired(message='Digite seu e-mail.'), Length(min=4, max=50)])
    submit = SubmitField('Enviar')