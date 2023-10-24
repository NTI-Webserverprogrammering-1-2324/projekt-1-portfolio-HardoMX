""" This script is used to register all routes of the portfolio """

from flask import Flask, render_template

from blueprints.home import home_bp


def create_app():
    app = Flask(__name__)
    
    
    #Register blueprints
    app.register_blueprint(home_bp)
    
    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")
    
    return app