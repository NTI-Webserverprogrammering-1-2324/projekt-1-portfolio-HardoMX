""" This script is use to render the Home-page of the portfolio """

from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)


@home_bp.route("/", methods=["GET"])
def home():
    return render_template("home.html", title="Home")