""" Blueprint for the login page. """
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user
from blueprints.data.lists import users
from blueprints.data.userClass import User

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET"])
def login():
    """Render the login page.

    Returns:
        The rendered login page.
    """

    return render_template("login.html")

@login_bp.route("/login", methods=["POST"])
def login_post():
    """Log in the user.

    Returns:
        The rendered login page.
    """

    username = request.form.get("username")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    if username not in users or users[username]["password"] != password:
        flash("Invalid username or password")
        return redirect(url_for("login.login"))

    user = User()
    login_user(user, remember=remember)

    return redirect(url_for("cms.cms"))
