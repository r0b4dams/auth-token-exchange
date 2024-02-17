from flask import Blueprint
from .controllers import *

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/callback", methods=["GET"])
def callback():
    return handle_callback()


@auth_blueprint.route("/login", methods=["GET"])
def login():
    return handle_login()


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return handle_logout()


@auth_blueprint.route("/refresh", methods=["POST"])
def refresh():
    return handle_refresh()


@auth_blueprint.route("/register", methods=["GET"])
def register():
    return handle_register()


@auth_blueprint.route("/user", methods=["GET"])
def user():
    return handle_user()
