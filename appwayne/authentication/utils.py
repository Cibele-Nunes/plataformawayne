from functools import wraps
from flask import abort
from flask_security import current_user

def permission_required(permission_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_permissions = set()
            for role in current_user.roles:
                for perm in role.permissions:
                    user_permissions.add(perm.name)
            if permission_name not in user_permissions:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
