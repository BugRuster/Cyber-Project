from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importing the routes (You will define these in `routes.py`)
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
