from flask import render_template, Blueprint, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
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
    if form.validate_on_submit():
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        user_nome = form.user_nome.data
        email = form.email.data
        hashed_senha = generate_password_hash(form.senha.data)
        newsletter = form.newsletter.data

        novo_usuario = Register(nome=nome, sobrenome=sobrenome, user_nome=user_nome, email=email, senha=hashed_senha, newsletter=newsletter)
        
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
                
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)
    
@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_nome = form.user_nome.data
        print(form.user_nome.data)
        senha = form.senha.data
        print(form.senha.data)
        
        usuario = db.session.query(Register).filter_by(user_nome='jogarcia').first()
        print(usuario)

        if usuario is None or not check_password_hash(usuario.senha, senha):
            flash('Usuário ou senha incorreto.', 'danger')
            return redirect(url_for('main.login'))
        
        login_user(usuario)
        flash('Login bem sucedido!', 'success')
        return redirect(url_for('main.users', nome=usuario.nome))
    return render_template('login.html', form=form)

@main_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_blueprint.route('/users/<nome>')
def users(nome):
    return render_template('users.html', nome=nome)


#@main_blueprint.route('/logout', methods = ['GET', 'POST'])
#@login_required

