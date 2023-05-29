from flask import Blueprint, render_template
from flask_login import login_required, current_user

general = Blueprint("general", __name__, template_folder='templates')

@general.route("/")
def greetings():
    return render_template("general/greetings.html")


@general.route("/home")
# @login_required
def home():
    return render_template("general/home.html")

