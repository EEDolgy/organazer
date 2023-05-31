from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(150), unique=True)
      password = db.Column(db.String(150))
      date_created = db.Column(db.DateTime(timezone=True), default=func.now())
      contents = db.relationship('Content', backref='user', passive_deletes=True)


class Content(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      date_created = db.Column(db.DateTime(timezone=True), default=func.now())
      text = db.Column(db.Text)
      type = db.Column(db.Enum('films', 'books', 'todo'), default='todo')
      author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

