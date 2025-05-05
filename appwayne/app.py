from flask import Flask
import pymysql
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import config_value
from appwayne.database import db, security, migrate
from appwayne.models import Role, User
from appwayne.auth import lm, session
from appwayne.config import Config
from dotenv import load_dotenv


"""Esta aplicação é relativa ao projeto da plataforma wayne."""
__version__="0.0.1"

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    lm.init_app(app)
    migrate.init_app(app, db)
    user_datastore = SQLAlchemyUserDatastore(db.session, User, Role)
    security.init_app(app, user_datastore)
    
    
    

    
    
    with app.app_context(): 
        from appwayne.views import main_blueprint 
        app.register_blueprint(main_blueprint)
    
    return app

