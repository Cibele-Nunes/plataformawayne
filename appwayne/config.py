import os
from dotenv import load_dotenv
from appwayne.forms import LoginForm, RegistrationForm

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
caminho_para_env = os.path.join(BASE_DIR, '.env')

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_LOGIN_USER_TEMPLATE = 'app_login.html'
    SECURITY_LOGIN_FORM = LoginForm
    SECURITY_REGISTER_USER_TEMPLATE = 'app_register.html'
    SECURITY_REGISTER_FORM = RegistrationForm
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURIT_USE_REGISTER_V2 = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_PASSWORD_RESET_EMAIL = True
    SECURITY_PASSWORD_SALT = os.environ.get('SALT')
    