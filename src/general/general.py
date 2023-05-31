from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import Content
from .. import db
from sqlalchemy import desc


general = Blueprint("general", __name__, template_folder='templates')

@general.route("/")
def greetings():
    return render_template("general/greetings.html", user=current_user)


@general.route("/home")
@login_required
def home():
    notes = Content.query.filter_by(author=current_user.id).order_by(desc(Content.date_created))
    return render_template("general/home.html", user=current_user, notes=notes)

@general.route("/add-note", methods=['POST', 'GET'])
@login_required
def add_note():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('A note can not be empty', category='error')
        else:
            cont = Content(text=text, author=current_user.id)

            db.session.add(cont)
            db.session.commit()

            flash('Note created', category='success')

            return redirect(url_for('general.home'))


    return render_template("general/add-note.html", user=current_user)

