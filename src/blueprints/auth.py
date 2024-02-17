"""blueprints.auth"""

from flask import Blueprint
import controllers.auth as auth_ctlr


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/callback", methods=["GET"])
def callback():
    return auth_ctlr.callback.handle_callback()


@auth_blueprint.route("/login", methods=["GET"])
def login():
    return auth_ctlr.login.handle_login()


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return auth_ctlr.logout.handle_logout()


@auth_blueprint.route("/refresh", methods=["POST"])
def refresh():
    return auth_ctlr.refresh.handle_refresh()


@auth_blueprint.route("/register", methods=["GET"])
def register():
    return auth_ctlr.register.handle_register()


@auth_blueprint.route("/user", methods=["GET"])
def user():
    return auth_ctlr.user.handle_user()
