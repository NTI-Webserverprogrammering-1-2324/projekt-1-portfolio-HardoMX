""" This script renders a simple Content Management System """

from flask import Blueprint, render_template, request, redirect, url_for
from blueprints.data.lists import what_entries, who_entries, messages



cms_bp = Blueprint("cms", __name__)



@cms_bp.route("/cms", methods=["GET"])
def cms():
    """
    Renders the CMS (Content Management System) page.

    This function returns the rendered HTML template for the CMS page.

    Returns:
        str: The rendered HTML template for the CMS page.
    """
    return render_template("cms.html")


# ================== CMS ==================

@cms_bp.route("/cms/about", methods=["GET"])
def cms_about():
    """Render the CMS about page.

    Returns:
        The rendered CMS about page.
    """
    return render_template("cms_about.html", who_entries=who_entries, what_entries=what_entries)


@cms_bp.route("/cms/about/create", methods=["POST"])
def add_content():
    """Add content to the CMS about page.

    Returns:
        The rendered CMS about page with the new content.
    """

    print(request.form)
    title = request.form["title"]
    text = request.form["text"]
    is_active = "isActive" in request.form

    which_list = "what-do" in request.form

    new_content = {
        "id": len(who_entries) + 1,
        #This creates a bug where the id is not unique if a message is deleted
        #If you remove by place instead of ID, or if ID can be given from 
        #an ever-increasing constant this bug is fixed!!!!!!!!
        "title": title,
        "text": text,
        "isActive": is_active
    }

    if which_list:
        what_entries.append(new_content)
    else:
        who_entries.append(new_content)

    return redirect(url_for("cms.cms_about"))


#@cms_bp.route("/cms/about/edit", methods=["POST"])


# ================== Contact ==================

@cms_bp.route("/cms/contact", methods=["GET"])
def cms_contact():
    """Render the CMS contact page.

    Returns:
        The rendered CMS contact page.
    """

    return render_template("cms_contact.html", messages=messages, length=len(messages))


@cms_bp.route("/cms/contact/msg_delete", methods=["POST"])
def delete_message():
    """Delete content from the CMS messages page.

    Returns:
        The rendered CMS about page without the deleted message.
    """

    print(request.form)
    msg_id = int(request.form["id"])

    for message in messages:
        if message["id"] == msg_id:
            messages.remove(message)
            break

    return redirect(url_for("cms.cms_contact"))
