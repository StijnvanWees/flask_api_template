from flask import Flask
from flask_cors import CORS
from src.auth_routes import auth_routes
from src.api_routes import *
from src.model.db import db, create_db
from waitress import serve
import sys
import os


def create_app(config_file="src/app/flask_app_settings.py"):
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": os.getenv("CORS_ORIGIN_URL")}})
    app.config.from_pyfile(config_file)

    app.register_blueprint(auth_routes)
    api.init_app(app)
    db.init_app(app)

    if "make_db" in sys.argv:
        create_db(app, "make_default_user" in sys.argv)

    return app


if __name__ == "__main__":
    app = create_app()

    if "production" in sys.argv:
        serve(app, host=os.getenv("APP_HOST"), port=int(os.getenv("APP_PORT")))
    else:
        app.run(debug=True)
