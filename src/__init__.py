from flask import Flask
from .general import general
from .auth import auth
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    app.register_blueprint(general, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # login_manager = LoginManager()
    # login_manager.login_view = "auth.login"
    # login_manager.init_app(app)
    #
    # @login_manager.user_loader
    # def load_user(id):
    #     return id

    return app