from flask import Blueprint
from .controller import AuthController

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
auth_controller = AuthController()


@auth_blueprint.route("/callback", methods=["GET"])
def callback():
    return auth_controller.callback()


@auth_blueprint.route("/login", methods=["GET"])
def login():
    return auth_controller.login()


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return auth_controller.logout()


@auth_blueprint.route("/refresh", methods=["POST"])
def refresh():
    return auth_controller.refresh()


@auth_blueprint.route("/register", methods=["GET"])
def register():
    return auth_controller.register()


@auth_blueprint.route("/user", methods=["GET"])
def user():
    return auth_controller.user()
