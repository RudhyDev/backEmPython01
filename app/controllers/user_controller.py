from flask import jsonify, request
from app.services.users_service import UserService

user_service = UserService()


def create_user():
    user_data = request.json
    user = user_service.create_user(user_data)
    return jsonify(user.serialize()), 201


def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.serialize() for user in users])


def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.serialize())


def update_user(user_id):
    user_data = request.json
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_service.update_user(user, user_data)
    return jsonify(user.serialize())


def delete_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_service.delete_user(user)
    return jsonify({'message': 'User deleted'})
