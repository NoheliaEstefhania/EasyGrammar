from flask import Flask
from .routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Registrar rutas y servicios
    register_routes(app)

    return app
