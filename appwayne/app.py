import os
from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from importlib import import_module
from appwayne.authentication.database import db, security, migrate
from appwayne.authentication.models import Role, User
from appwayne.authentication.auth import lm
from appwayne.config import Config
from dotenv import load_dotenv


"""Esta aplicação é relativa ao projeto da plataforma wayne."""
__version__="0.0.1"

load_dotenv()

def register_extensions(app):
    db.init_app(app)
    lm.init_app(app)
    migrate.init_app(app, db)

    user_datastore = SQLAlchemyUserDatastore(db.session, User, Role)
    security.init_app(app, user_datastore)
    
def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('appwayne.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)

    return app

