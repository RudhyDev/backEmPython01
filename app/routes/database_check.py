from flask import Blueprint, jsonify
from sqlalchemy import text
from app import db

database_check_bp = Blueprint('database_check', __name__)


@database_check_bp.route('/database-check', methods=['GET'])
def database_check():
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
        return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
