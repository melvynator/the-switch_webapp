# Import flask dependencies
from flask import Blueprint, render_template


module_general = Blueprint('general', __name__, url_prefix='')


@module_general.route('/home/', methods=['GET'])
def home():
    return render_template("home/home.html")
