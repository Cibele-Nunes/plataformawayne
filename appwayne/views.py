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
    
@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login bem sucedido!', 'sucess')
        return redirect(url_for('templates.users'))
    return render_template('login.html', form=form)
