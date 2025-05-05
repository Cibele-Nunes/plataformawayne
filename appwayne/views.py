from flask import render_template, Blueprint, flash, request, redirect, url_for, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask_security import roles_accepted
from flask_security.utils import send_mail
from appwayne.models import User, Role
from appwayne.database import db
from appwayne.forms import RegistrationForm, LoginForm, ForgotPasswordForm

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
def home():
    return render_template('home.html')

@main_blueprint.route('/app_register', methods=['GET', 'POST'])
def app_register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        user_nome = form.user_nome.data
        email = form.email.data
        hashed_senha = generate_password_hash(form.senha.data)
        newsletter = form.newsletter.data

        novo_usuario = db.session.query(User).filter_by(user_nome=user_nome).first()
        if novo_usuario:
            flash('Usuário já existe.')
            return render_template("app_register.html")

        novo_usuario = User(nome=nome, sobrenome=sobrenome, user_nome=user_nome, email=email, senha=hashed_senha, newsletter=newsletter)
        novo_usuario.active = True

        role = db.session.query(Role).filter_by(nome=nome).first()
        if role:
            novo_usuario.roles.append(role)
        else:
            flash('Função selecionada inválida.')
            return render_template("app_register.html")
        
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('main.app_login'))
    return render_template('app_register.html', register_user_form=form)
    
@main_blueprint.route('/app_login', methods=['GET', 'POST'])
def app_login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_nome = form.user_nome.data
        senha = form.senha.data
                        
        usuario = db.session.query(User).filter_by(user_nome=user_nome).first()
        if usuario:
            if usuario is None or not check_password_hash(usuario.senha, senha):
                flash('Usuário ou senha incorreto.', 'danger')
                return redirect(url_for('main.app_login'))
            
            if usuario.senha == form.senha.data['senha']:
                login_user(usuario, remember=form.lembre_me.data)
                return redirect(url_for('main.users', nome=usuario.nome))
        
    return render_template('app_login.html', login_user_form=form)

@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main_blueprint.route('/usuarios/<nome>')
@login_required
def users(nome):
    return render_template('usuarios.html', nome=nome)

@main_blueprint.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password_view():
    forgot_password_form = ForgotPasswordForm()
    if forgot_password_form.validate_on_submit():
        email = forgot_password_form.email.data

        usuario = db.session.query(User).filter_by(email=email).first()

        if usuario:
            security = current_app.extensions["security"]
            token = security.generate_password_reset_token(usuario)

            send_mail('reset_password', usuario, token=token)
            flash('Instruções de redefinição de senha foram enviadas para o seu e-mail.', 'success')
            session['password_reset_email'] = email
        else:
            flash('E-mail não encontrado.', 'danger')
        return redirect(url_for('main.forgot_password_view'))
    return render_template('forgot_password.html', forgot_password_form=forgot_password_form)

@main_blueprint.route('/forgot_password/reenviar')
def forgot_password_reenviar():
    email = session.get('password_reset_email')
    if not email:
        flash('Nenhum e-mail fornecido para reenvio.', 'danger')
        return redirect(url_for('main.forgot_password_view'))
    usuario = db.session.query(User).filter_by(email=email).first()
    if usuario:
        security = current_app.extensions["security"]
        token = security.generate_password_reset_token(usuario)
        send_mail('reset_password', usuario, token=token)
        flash('E-mail de redefinição de senha foi reenviado com sucesso.', 'success')
    else:
        flash('E-mail não encontrado.', 'danger')
    return redirect(url_for('main.forgot_password_view'))