from flask import jsonify, request
from app.services.auth_service import AuthService


def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    authenticated = AuthService.login(email, password)
    if authenticated:
        # Implemente a lógica de geração de token de autenticação aqui
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


def logout():
    AuthService.logout()
    return jsonify({'message': 'Logged out successfully'}), 200
