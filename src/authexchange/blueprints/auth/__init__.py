import flask

from . import controllers as ctl


auth_blueprint = flask.Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/callback", methods=["GET"])
def callback():
    return ctl.callback.handle_callback()


@auth_blueprint.route("/register", methods=["GET"])
def register():
    return ctl.signup_login.handle_signup()


@auth_blueprint.route("/login", methods=["GET"])
def login():
    return ctl.signup_login.handle_login()


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    return ctl.logout.handle_logout()


@auth_blueprint.route("/refresh", methods=["POST"])
def refresh():
    return ctl.refresh.handle_refresh()


@auth_blueprint.route("/user", methods=["GET"])
def user():
    return ctl.user.handle_user()
