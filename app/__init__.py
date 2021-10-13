from flask import Flask
from os import path
from app.models import *

def create_app():
    app = Flask(__name__)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
    from .views import views
    from .api import api
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api,url_prefix='/')
    return app