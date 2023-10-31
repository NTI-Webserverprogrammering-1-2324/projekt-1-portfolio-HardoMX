""" This script is used to render the Code-page for the portfolio website """

from flask import Blueprint, render_template

code_bp = Blueprint('code', __name__)

@code_bp.route('/code', methods=['GET'])
def code():
    """ Return code page """
    return render_template('code.html', title="Code")
