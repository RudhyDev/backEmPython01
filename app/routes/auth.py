from flask import Blueprint
from app.controllers.auth_controller import login, logout

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/logout', methods=['POST'])(logout)


def register_auth_routes(app):
    app.register_blueprint(auth_bp)
