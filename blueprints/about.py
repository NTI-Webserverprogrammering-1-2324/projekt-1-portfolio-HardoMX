""" This script is used to render the about-page of the portfolio """

from flask import Blueprint, render_template
from blueprints.cms import who_entries, what_entries

about_bp = Blueprint('about', __name__)


@about_bp.route("/about", methods=["GET"])
def about():
    """ Return about page """
    return render_template("about.html", title="About", who_entries=who_entries, what_entries=what_entries)
