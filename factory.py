""" This script is used to register all routes of the portfolio """

from flask import Flask, render_template
import flask_login
from blueprints.data.userClass import User

from blueprints.home import home_bp
from blueprints.about import about_bp
from blueprints.code import code_bp
from blueprints.cms import cms_bp
from blueprints.login import login_bp


def create_app():
    """ Registers all routes of the site """
    app = Flask(__name__)
    app.secret_key = "c1f03512ccb3c5890ee5317034f4dbf9027bd29e7ab749a8c10153ffdbf82851"

    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'login.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        user = User()
        user.id = user_id
        return user


    #Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(code_bp)
    app.register_blueprint(cms_bp)
    app.register_blueprint(login_bp)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    return app
