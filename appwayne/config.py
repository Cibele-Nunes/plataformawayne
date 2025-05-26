import os, random, string
from dotenv import load_dotenv
from appwayne.authentication.forms import LoginForm, RegistrationForm

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
caminho_para_env = os.path.join(BASE_DIR, '.env')

class Config:
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY = os.environ.get('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice(string.ascii_lowercase) for _ in range(32))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE   = os.getenv('DB_ENGINE')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASS     = os.getenv('DB_PASS')
    DB_HOST     = os.getenv('DB_HOST')
    DB_PORT     = os.getenv('DB_PORT')
    DB_NAME     = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        DB_ENGINE,
        DB_USERNAME,
        DB_PASS,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )
    
    SECURITY_LOGIN_USER_TEMPLATE = 'app_login.html'
    SECURITY_LOGIN_FORM = LoginForm
    SECURITY_REGISTER_USER_TEMPLATE = 'app_register.html'
    SECURITY_REGISTER_FORM = RegistrationForm
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURIT_USE_REGISTER_V2 = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_PASSWORD_RESET_EMAIL = True
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', 'SALT')

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Dicionário de configurações
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
    