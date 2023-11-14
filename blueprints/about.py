""" This script is used to render the about-page of the portfolio """

from flask import Blueprint, render_template, redirect, url_for, request
from blueprints.data.lists import who_entries, what_entries, messages

about_bp = Blueprint('about', __name__)



@about_bp.route("/about", methods=["GET"])
def about():
    """ Return about page """
    return render_template("about.html", title="About",
                            who_entries=who_entries, what_entries=what_entries)

#To avoid two messages  sharing the same ID if one is deleted,
#we use a global variable that is always increased by 1 when a new message is added.
MESSAGE_ID = 1

@about_bp.route("/about/contact", methods=["POST"])
def contact():
    """Render the contact page.

    Returns:
        The rendered contact page as a string.
    """

    print(request.form)
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    global MESSAGE_ID

    new_message = {
        "id": MESSAGE_ID,
        "name": name,
        "email": email,
        "message": message
    }

    MESSAGE_ID += 1

    messages.append(new_message)

    return redirect(url_for("about.about"))
