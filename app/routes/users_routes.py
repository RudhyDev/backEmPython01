from flask import Blueprint
from app.controllers.user_controller import (
    create_user, get_all_users, get_user_by_id, update_user, delete_user
)

users_bp = Blueprint('users', __name__, url_prefix='/users')

users_bp.route('/', methods=['POST'])(create_user)
users_bp.route('/', methods=['GET'])(get_all_users)
users_bp.route('/<int:user_id>', methods=['GET'])(get_user_by_id)
users_bp.route('/<int:user_id>', methods=['PUT'])(update_user)
users_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user)


def register_user_routes(app):
    app.register_blueprint(users_bp)
