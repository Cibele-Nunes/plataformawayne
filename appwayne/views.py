from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_user
from appwayne.models import Register
from appwayne.database import db
from appwayne.forms import RegistrationForm, LoginForm

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def home():
    return render_template('home.html')

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        user_nome = form.user_nome.data
        email = form.email.data
        senha = form.senha.data
        confirm_senha = form.confirm_senha.data
        newsletter = form.newsletter.data

        novo_usuario = Register(nome=nome, sobrenome=sobrenome, user_nome=user_nome, email=email, senha=senha, confirm_senha=confirm_senha, newsletter=newsletter)
        
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)
        
        return render_template('login_visit.html')
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
