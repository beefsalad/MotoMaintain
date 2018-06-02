import os
from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from backend.app.resources.user import UserRegister

basedir = os.path.dirname(__file__)
static = os.path.join(basedir, '../../dist/static')
template = os.path.join(basedir, '../../dist')
settings = os.path.join(basedir, '../settings.py')

db = SQLAlchemy()


def create_app():
    app = Flask(__name__,
                static_folder=static,
                template_folder=template)
    api = Api(app)

    app.config.from_pyfile(settings)

    api.add_resource(UserRegister, '/register')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")

    return app
