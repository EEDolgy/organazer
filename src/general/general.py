from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from ..models import Content
from .. import db


general = Blueprint("general", __name__, template_folder='templates')

@general.route("/")
def greetings():
    return render_template("general/greetings.html", user=current_user)


@general.route("/home")
@login_required
def home():
    notes = Content.query.all()
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


    return render_template("content/add-note.html", user=current_user)

