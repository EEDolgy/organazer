from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")

@auth.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash(f'Welcome, {username}!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('general.home'))
            else:
                flash('Password is incorrect', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("auth/login.html", user=current_user)


@auth.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            flash('This username already exists', category='error')
        elif username == '':
            flash('Username can not be empty', category='error')
        elif password1 == '':
            flash('Password can not be empty', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        else:
            user = User(username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('User created!')
            return redirect(url_for('general.home'))

    return render_template("auth/sign-up.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("general.greetings"))