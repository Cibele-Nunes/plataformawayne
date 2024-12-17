from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from datetime import datetime
from appwayne.database import Base

class Register(Base):
    __tablename__ = 'registers'
    id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    DataCadastro = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    user_nome = mapped_column(String(50), nullable=False)
    nome = mapped_column(String(50), nullable=False)
    sobrenome = mapped_column(String(50), nullable=False)
    email = mapped_column(String(50), nullable=False, unique=True)
    telefone = mapped_column(String(20), nullable=False)
    senha = mapped_column(String(50), nullable=False)
    confirm_senha = mapped_column(String(50), nullable=False)

    def __init__(self, DataCadastro, user_nome, nome, sobrenome, email, telefone, senha, confirm_senha):
        self.DataCadastro = DataCadastro
        self.user_nome = user_nome
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.confirm_senha = confirm_senha
    
class Login(Base):
    __tablename__ = 'usuarios'
    id = mapped_column(Integer, ForeignKey('registers.id'), primary_key=True, nullable=False)
    user_nome = mapped_column(String(50), nullable=False)
    senha = mapped_column(String(50), nullable=False)
    
    def __init__(self, user_nome, senha):
        self.user_nome = user_nome
        self.senha = senha

