from flask import render_template, Blueprint, flash, redirect, url_for
from flask_wtf import FlaskForm
from appwayne.forms import RegisterForm, LoginForm

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def home():
    return render_template('home.html')

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
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
