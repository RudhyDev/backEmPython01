from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize database object
db = SQLAlchemy()

migrate = Migrate()


def register_routes(app):
    from app.routes.health_check import health_check_bp
    from app.routes.database_check import database_check_bp
    from app.routes.auth import auth_bp
    from app.routes.users_routes import register_user_routes

    app.register_blueprint(health_check_bp)
    app.register_blueprint(database_check_bp)
    app.register_blueprint(auth_bp)
    register_user_routes(app)

    # Register other routes here...


# Function to create the Flask app
def create_app(config_class=Config):
    # Create the Flask app
    app = Flask(__name__)

    # Load configurations from config.py
    app.config.from_object(config_class)

    # Initialize app for SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    register_routes(app)

    # Return the app instance
    return app
