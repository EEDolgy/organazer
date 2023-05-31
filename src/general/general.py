from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Content

general = Blueprint("general", __name__, template_folder='templates')

@general.route("/")
def greetings():
    return render_template("general/greetings.html", user=current_user)


@general.route("/home")
@login_required
def home():
    contents = Content.query.all()
    return render_template("general/home.html", user=current_user, contents=contents)

