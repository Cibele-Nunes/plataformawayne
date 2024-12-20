from flask import render_template, Blueprint, flash, redirect, url_for, request
from appwayne.models import Register
from appwayne.database import db
from appwayne.forms import RegisterForm, LoginForm

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def home():
    return render_template('home.html')

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        DataCadastro = request.form['DataCadastro']
        user_nome = request.form['user_nome']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']

        usuario = Register(DataCadastro=DataCadastro, user_nome=user_nome, nome=nome, sobrenome=sobrenome, email=email, telefone=telefone, senha=senha, confirm_senha=confirm_senha)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('login_visit.html'))

    form = RegisterForm()
    if form.validate_on_submit():
        flash('Cadastro feito com sucesso!', 'sucess')
        return redirect(url_for('templates.login'))
    return render_template('register.html', form=form)
    
@main_blueprint.route('/login_visit', methods=['GET', 'POST'])
def login_visit():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login bem sucedido!', 'sucess')
        return redirect(url_for('templates.users_visit'))
    return render_template('login_visit.html', form=form)

@main_blueprint.route('/users_visit/<nome>')
def users_visit(nome):
    return render_template('users_visit.html', nome=nome)
