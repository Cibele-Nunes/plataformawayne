import uuid
from datetime import date
from flask_security import UserMixin, RoleMixin
from appwayne.authentication.database import db


# Associação many-to-many entre usuários e funções (roles)
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

# Associação many-to-many entre funções e permissões
role_permissions = db.Table(
    'role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    # Permissões que essa função concede
    permissions = db.relationship(
        'Permission',
        secondary=role_permissions,
        backref=db.backref('roles', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Role {self.name!r}>'


class Permission(db.Model):
    __tablename__ = 'permission'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Permission {self.name!r}>'


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    # --- Identificação e Segurança ---
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DataCadastro      = db.Column(db.Date,    default=date.today, nullable=False)
    user_nome         = db.Column(db.String(50), unique=True, nullable=False)
    senha             = db.Column(db.String(260),             nullable=False)
    active            = db.Column(db.Boolean, default=True,   nullable=False)
    fs_uniquifier     = db.Column(db.String(255), unique=True, nullable=False,
                                   default=lambda: uuid.uuid4().hex)
    confirmed_at      = db.Column(db.Date,    nullable=True)
    last_login_at     = db.Column(db.Date,    nullable=True)
    current_login_at  = db.Column(db.Date,    nullable=True)
    last_login_ip     = db.Column(db.String(100), nullable=True)
    current_login_ip  = db.Column(db.String(100), nullable=True)
    login_count       = db.Column(db.Integer,   default=0)
    # (Você pode incluir aqui seus campos de 2FA, se quiser)

    # --- Contato e Identificação Pessoal ---
    nome              = db.Column(db.String(50),  nullable=False)
    sobrenome         = db.Column(db.String(50),  nullable=True)
    nome_social       = db.Column(db.String(50),  nullable=True)
    ident_genero      = db.Column(db.String(20),  nullable=True)
    email             = db.Column(db.String(80),  unique=True, nullable=False)
    celular           = db.Column(db.String(20),  nullable=True)
    num_whatsapp      = db.Column(db.String(20),  nullable=True)
    data_nasc         = db.Column(db.Date,        nullable=True)
    est_civil         = db.Column(db.String(20),  nullable=True)
    filhos            = db.Column(db.Boolean, default=False)
    num_filhos        = db.Column(db.Integer,      nullable=True)
    formacao          = db.Column(db.String(100), nullable=True)

    # --- Endereço ---
    cep               = db.Column(db.String(9),    nullable=True)
    rua               = db.Column(db.String(120),  nullable=True)
    numero            = db.Column(db.String(10),   nullable=True)
    bairro            = db.Column(db.String(50),   nullable=True)
    cidade            = db.Column(db.String(50),   nullable=True)
    estado            = db.Column(db.String(2),    nullable=True)

    # --- Dados Contratuais ---
    data_admissao     = db.Column(db.Date,   nullable=True)
    salario           = db.Column(db.Float,  nullable=True)
    jornada           = db.Column(db.String(50), nullable=True)
    cpf               = db.Column(db.String(14), unique=True, nullable=False)
    rg                = db.Column(db.String(20),  nullable=False)
    cart_trab         = db.Column(db.String(30),  nullable=False)
    pis               = db.Column(db.String(20),  nullable=False)

    # --- Informações Complementares ---
    observacoes       = db.Column(db.Text, nullable=True)

    # --- Relacionamentos ---
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, **kwargs):
        """
        Permite inicializar User com qualquer subset de colunas.
        Ex.: User(nome='Ana', sobrenome='Silva', email='ana@ex.com', ...)
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return f'<User {self.user_nome!r}>'
