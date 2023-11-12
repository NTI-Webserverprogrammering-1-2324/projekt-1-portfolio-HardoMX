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

    which_list = request.form["which_list"]


    if which_list == "What":
        new_content = {
        "id": len(what_entries) + 1,
        #This creates a bug where the id is not unique if a message is deleted.
        #This affects both deleting and editing.
        #If you remove by place instead of ID, or if ID can be given from
        #an ever-increasing constant this bug is fixed!!!!!!!!
        "title": title,
        "text": text,
        "isActive": is_active
        }

        what_entries.append(new_content)

    else:
        new_content = {
        "id": len(who_entries) + 1,
        #This creates a bug where the id is not unique if a message is deleted.
        #This affects both deleting and editing.
        #If you remove by place instead of ID, or if ID can be given from
        #an ever-increasing constant this bug is fixed!!!!!!!!
        "title": title,
        "text": text,
        "isActive": is_active
        }

        who_entries.append(new_content)

    return redirect(url_for("cms.cms_about"))


@cms_bp.route("/cms/about/active", methods=["POST"])
def toggle_active():
    """Toggle the active state of a content item on the CMS about page.

    Returns:
        The rendered CMS about page with the toggled active state.
    """

    print(request.form)
    content_id = int(request.form["id"])
    list_name = request.form["list"]

    if list_name == "who":
        for content in who_entries:
            if content["id"] == content_id:
                content["isActive"] = not content["isActive"]
                break
    else:
        for content in what_entries:
            if content["id"] == content_id:
                content["isActive"] = not content["isActive"]
                break

    return redirect(url_for("cms.cms_about"))


@cms_bp.route("/cms/about/edit", methods=["POST"])
def edit_content():
    """Edit the title and text of a content entry.

    This function retrieves the ID, list name, title, and text of a content entry from the request form,
    and updates the corresponding entry in either the "who" or "what" list of entries. The updated entry
    is identified by its ID. Finally, the function redirects to the "cms_about" endpoint.

    Returns:
        A redirect response to the "cms_about" endpoint.
    """

    print(request.form)
    content_id = int(request.form["id"])
    list_name = request.form["list"]
    title = request.form["title"]
    text = request.form["text"]

    if list_name == "who":
        for content in who_entries:
            if content["id"] == content_id:
                content["title"] = title
                content["text"] = text
                break
    else:
        for content in what_entries:
            if content["id"] == content_id:
                content["title"] = title
                content["text"] = text
                break

    return redirect(url_for("cms.cms_about"))


@cms_bp.route("/cms/about/delete", methods=["POST"])
def delete_content():
    """Delete content from the CMS about page.

    Returns:
        The rendered CMS about page without the deleted content.
    """

    print(request.form)
    content_id = int(request.form["id"])
    list_name = request.form["list"]

    if list_name == "who":
        for content in who_entries:
            if content["id"] == content_id:
                who_entries.remove(content)
                break
    else:
        for content in what_entries:
            if content["id"] == content_id:
                what_entries.remove(content)
                break

    return redirect(url_for("cms.cms_about"))


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
