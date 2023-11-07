""" This script renders a simple Content Management System """

from flask import Blueprint, render_template, request, redirect, url_for

#Create list to store site changes
who_entries = []
what_entries = []

cms_bp = Blueprint("cms", __name__)



@cms_bp.route("/cms", methods=["GET"])
def cms():
    """ Return the CMS page """
    return render_template("cms.html")

@cms_bp.route("/cms/about", methods=["GET"])
def cms_about():
    return render_template("cms_about.html", who_entries=who_entries)