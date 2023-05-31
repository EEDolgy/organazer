from flask import Blueprint, render_template
from flask_login import current_user, login_required


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


@content.route("/add-note")
@login_required
def add_note():
    return render_template("content/add-note.html", user=current_user)
