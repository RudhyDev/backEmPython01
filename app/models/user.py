"""
Módulo: user.py
Autor: Rudhy
Data de Criação:01/07/2023
Descrição: Este módulo contém a definição da classe User, que representa a entidade de usuário no banco de dados.
"""

from app import db


class User(db.Model):
    """
    Classe User.

    A classe User define a estrutura e o comportamento de um usuário no sistema.

    Atributos:
        id (int): O ID do usuário (chave primária).
        name (str): O nome do usuário.
        email (str): O endereço de e-mail do usuário (deve ser único).
        password (str): A senha do usuário.

    Métodos:
        __repr__(): Retorna uma representação em string do objeto User.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        """
        Retorna uma representação em string do objeto User.

        Retorna:
            str: representação em string do objeto User.
        """
        return '<User {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
