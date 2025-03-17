from flask import render_template, Blueprint, flash, redirect, url_for, request
from appwayne.models import Register
from appwayne.database import db
from appwayne.forms import RegistrationForm, LoginForm

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def home():
    return render_template('home.html')

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_nome = request.form['user_nome']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']
        newsletters = request.form['newsletters']

        usuario = Register(user_nome=user_nome, nome=nome, sobrenome=sobrenome, email=email, senha=senha, confirm_senha=confirm_senha, newsletters=newsletters)
        
        db.session.add(usuario)
        db.session.commit()
        
        return render_template('login_visit.html')

    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Cadastro feito com sucesso!', 'sucess')
        return redirect(url_for('login_visit.html'))
    return render_template('register.html', form=form)
    
@main_blueprint.route('/login_visit', methods=['GET', 'POST'])
def login_visit():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login bem sucedido!', 'sucess')
        return redirect(url_for('users_visit.html'))
    return render_template('login_visit.html', form=form)

@main_blueprint.route('/users_visit/<nome>')
def users_visit(nome):
    return render_template('users_visit.html', nome=nome)
