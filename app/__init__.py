from flask import Flask
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)

    from app.urls import __URLPATH__

    __URLPATH__()

    api.init_app(app)

    return app
