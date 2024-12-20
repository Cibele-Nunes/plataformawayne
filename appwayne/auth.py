from flask_login import LoginManager

lm = LoginManager()

@lm.user_loader()
def user_loader(id):
    return 'Vamos a diante!'