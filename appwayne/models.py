from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Date, Table
import json
import uuid
from datetime import date
from sqlalchemy.orm import relationship
from flask_security import UserMixin, RoleMixin
from flask_security.models import sqla
from appwayne.database import Base, db

sqla.FsModels.set_db_info(base_model=Base)

# Tabela associativa entre Role e Permission
role_permissions = db.Table(
    'role_permissions',
    db.Column('role_id', Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', Integer, db.ForeignKey('permission.id'), primary_key=True)
)

class Role(Base, sqla.FsRoleMixin):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(250), nullable=False)

    def __init__(self, name, description):
        """
        :param name: Nome da função, por exemplo, "presidente".
        :param description: Descrição detalhada da função.
        :param permissions: Lista (Python) de permissões (strings) que serão serializadas em JSON.
                            Se None, assume uma lista vazia.
        """
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Role: {self.name}>'

    @property
    def permissions_list(self):
        """Retorna as permissões como uma lista Python."""
        try:
            return json.loads(self.permissions)
        except Exception:
            return []
    
    @permissions_list.setter
    def permissions_list(self, perm_list):
        """Define as permissões a partir de uma lista Python."""
        self.permissions = json.dumps(perm_list)
    
    def __repr__(self):
        return f'<Role: {self.name} | {self.description}>'

# Exemplo de Modelo de Usuário, para referência e associação com as funções.
class User(Base, sqla.FsUserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True) 
    DataCadastro = Column(Date, default=date.today, nullable=False) 
    user_nome = Column(String(50), nullable=False, unique=True) 
    nome = Column(String(50), nullable=False) 
    sobrenome = Column(String(50), nullable=True) 
    email = Column(String(50), nullable=False) 
    senha = Column(String(260), nullable=False) 
    newsletter = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    fs_uniquifier = Column(String(255), unique=True, nullable=False, default=lambda: uuid.uuid4().hex)
    confirmed_at = Column(Date)
    last_login_at = Column(Date)
    current_login_at = Column(Date)
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer, default=0)
    tf_primary_method = Column(String(64), nullable=True)
    tf_totp_secret = Column(String(255), nullable=True)
    tf_phone_number = Column(String(64), nullable=True)
    us_totp_secrets = Column(String(255), nullable=True)
    us_phone_number = Column(String(64), nullable=True)
    fs_webauthn_user_handle = Column(String(255), nullable=True)
    mf_recovery_codes = Column(String(255), nullable=True)

    def __init__(self, user_nome, nome, sobrenome, email, senha, newsletter, active=True,
            fs_uniquifier=None, confirmed_at=None, last_login_at=None, 
            current_login_at=None, last_login_ip=None, current_login_ip=None,
            login_count=0, tf_primary_method=None, tf_totp_secret=None,
            tf_phone_number=None, us_totp_secrets=None, us_phone_number=None,
            fs_webauthn_user_handle=None, mf_recovery_codes=None, **kwargs):
        self.user_nome = user_nome
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.newsletter = newsletter
        self.active = active
        self.fs_uniquifier = fs_uniquifier
        self.confirmed_at = confirmed_at
        self.last_login_at = last_login_at
        self.current_login_at = current_login_at
        self.last_login_ip = last_login_ip
        self.current_login_ip = current_login_ip
        self.login_count = login_count
        self.tf_primary_method = tf_primary_method
        self.tf_totp_secret = tf_totp_secret
        self.tf_phone_number = tf_phone_number
        self.us_totp_secrets = us_totp_secrets
        self.us_phone_number = us_phone_number
        self.fs_webauthn_user_handle = fs_webauthn_user_handle
        self.mf_recovery_codes = mf_recovery_codes

        for key, value in kwargs.items():
            setattr(self, key, value)

 # Relação muitos-para-muitos com as funções (roles)
    roles = relationship('Role', secondary='roles_users', backref='users')
    
    def __repr__(self):
        return f'<User: {self.user_nome}>'

class Permission(Base):
    __tablename__ = 'permission'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(250), nullable=True)

 # Adiciona a relação muitos-para-muitos com Permission
    permissions = relationship('Permission', secondary=role_permissions, backref='roles')
    
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'<Permission: {self.name}>'

class Login(Base, UserMixin):
    __tablename__ = 'login'
    login_id = Column(Integer, primary_key=True, nullable=False)
    user_nome = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    
    def __init__(self, user_nome, senha):
        self.user_nome = user_nome
        self.senha = senha

