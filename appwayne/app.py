from flask import Flask
import pymysql
from flask_login import LoginManager
from appwayne.database import db, migrate
from dotenv import load_dotenv


"""Esta aplicação é relativa ao projeto da plataforma wayne."""
__version__="0.0.1"

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATION']

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    with app.app_context(): 
        from appwayne.views import main_blueprint 
        app.register_blueprint(main_blueprint)

    return app