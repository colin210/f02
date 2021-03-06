# coding: utf-8
from flask import Flask, render_template, request,send_from_directory
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .info import info as info_blueprint
    from .phone import phone as phone_blueprint
    from .leader import leader as leader_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(info_blueprint, url_prefix='/info')
    app.register_blueprint(phone_blueprint, url_prefix='/phone')
    app.register_blueprint(leader_blueprint, url_prefix='/leader')



    return app
