from flask_login import LoginManager
from sqlalchemy.orm import sessionmaker
from appwayne.database import db
from appwayne.models import User

lm = LoginManager()
lm.session_protection = "strong"
lm.login_view = "main.app_login"
lm.login_message_category = "info"

Session = sessionmaker(bind=db)
session = Session()

@lm.user_loader
def load_user(id):
    try:
        return session.query(User).filter_by(int(id)).first()
    except Exception:
        return None
    
