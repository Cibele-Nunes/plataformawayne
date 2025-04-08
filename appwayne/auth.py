from flask_login import LoginManager
from appwayne.database import Session
from appwayne.models import Register

lm = LoginManager()
lm.session_protection = "strong"
lm.login_view = "main.login"
lm.login_message_category = "info"

session = Session()


@lm.user_loader
def user_loader(id):
    try:
        return session.query(Register).filter_by(int(id)).first()
    except Exception:
        return None
    
