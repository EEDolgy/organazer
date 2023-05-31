from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from ..models import Content
from .. import db


content = Blueprint("content", __name__, template_folder='templates')


@content.route("/films")
@login_required
def films():
    return render_template("content/films.html", user=current_user)


@content.route("/books")
@login_required
def books():
    return render_template("content/books.html", user=current_user)


@content.route("/todo-list")
@login_required
def todo_list():
    return render_template("content/todo-list.html", user=current_user)


@content.route("/add-note", methods=['POST', 'GET'])
@login_required
def add_note():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('A note can not be empty', category='error')
        else:
            cont = Content(text=text, author=current_user.id, type='todo')

            db.session.add(cont)
            db.session.commit()

            flash('Note created', category='success')


    return render_template("content/add-note.html", user=current_user)
