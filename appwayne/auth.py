from flask_login import LoginManager
from appwayne.database import db
from appwayne.models import Register

lm = LoginManager()
lm.session_protection = "strong"
lm.login_view = "auth.login"
lm.login_message_category = "info"


@lm.user_loader()
def user_loader(id):
    try:
        return Register.query.filter_by(id=id).first()
    except:
        return None
    
