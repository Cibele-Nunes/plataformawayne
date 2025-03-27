from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from datetime import date
from flask_login import UserMixin
from appwayne.database import Base

class Register(Base, UserMixin):
    __tablename__ = 'registers'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True) 
    DataCadastro = Column(Date, default=date.today, nullable=False) 
    user_nome = Column(String(50), nullable=False, unique=True) 
    nome = Column(String(50), nullable=False) 
    sobrenome = Column(String(50), nullable=True) 
    email = Column(String(50), nullable=False) 
    senha = Column(String(50), nullable=False) 
    confirm_senha = Column(String(50), nullable=False)
    newsletter = Column(Boolean, nullable=False)


    def __init__(self, user_nome, nome, sobrenome, email, senha, confirm_senha, newsletter):
        self.user_nome = user_nome
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.confirm_senha = confirm_senha
        self.newsletter = newsletter
    
class Login(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, ForeignKey('registers.id'), primary_key=True, nullable=False)
    user_nome = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    
    def __init__(self, user_nome, senha):
        self.user_nome = user_nome
        self.senha = senha

