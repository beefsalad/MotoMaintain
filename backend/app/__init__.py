import os
from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from backend.db import db, ma
from flask_migrate import Migrate
from backend.app.resources.user import UserRegister, UserLogin

basedir = os.path.dirname(__file__)
static = os.path.join(basedir, '../../dist/static')
template = os.path.join(basedir, '../../dist')
settings = os.path.join(basedir, '../settings.py')


def create_app():
    app = Flask(__name__,
                static_folder=static,
                template_folder=template)
    api = Api(app)

    app.config.from_pyfile(settings)

    jwt = JWTManager(app)

    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")

    return app
