""" This script is used to render the about-page of the portfolio """

from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)


@about_bp.route("/about", methods=["GET"])
def about():
    """ Return about page """
    return render_template("about.html", title="Home")
