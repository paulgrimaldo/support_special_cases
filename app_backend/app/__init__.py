from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS

from app.framework.config import Config

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'custom_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': r'logs/app.log'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'custom_handler']
    }
})


def create_app():
    app = Flask(__name__,
                static_folder='../../app_frontend/dist/static',
                template_folder='../../app_frontend/dist'
                )

    app.config.from_object(Config)

    CORS(app, expose_headers=["x-suggested-filename"])

    return app
