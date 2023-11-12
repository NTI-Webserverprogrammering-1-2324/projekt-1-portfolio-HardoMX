""" This script is used to render the about-page of the portfolio """

from flask import Blueprint, render_template, redirect, url_for, request
from blueprints.data.lists import who_entries, what_entries, messages

about_bp = Blueprint('about', __name__)



@about_bp.route("/about", methods=["GET"])
def about():
    """ Return about page """
    return render_template("about.html", title="About",
                            who_entries=who_entries, what_entries=what_entries)


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

    new_message = {
        "id": len(messages) + 1, 
        #This creates a bug where the id is not unique if a message is deleted
        #If you remove by place instead of ID, or if ID can be given from
        #an ever-increasing constant this bug is fixed!!!!!!!!
        "name": name,
        "email": email,
        "message": message
    }

    messages.append(new_message)

    return redirect(url_for("about.about"))
