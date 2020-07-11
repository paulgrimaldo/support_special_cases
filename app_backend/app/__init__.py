from flask import Flask
from flask_cors import CORS

from app.framework.config import Config


def create_app():
    app = Flask(__name__,
                static_folder='../../app_frontend/dist/static',
                template_folder='../../app_frontend/dist'
                )

    app.config.from_object(Config)

    CORS(app, expose_headers=["x-suggested-filename"])

    return app
