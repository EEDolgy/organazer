from flask import Blueprint, render_template
from flask_login import login_required, current_user

auth = Blueprint("auth", __name__, template_folder="templates")

@auth.route("/login")
def login():
    return render_template("auth/login.html")


@auth.route("/sign-up")
def sign_up():
    return render_template("auth/sign-up.html")


@auth.route("/logout")
# @login_required
def logout():
    return render_template("auth/logout.html")