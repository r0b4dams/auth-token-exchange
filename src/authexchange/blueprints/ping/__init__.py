import flask

ping_blueprint = flask.Blueprint("ping", __name__, url_prefix="")


@ping_blueprint.route("/ping", methods=["GET"])
def ping():
    """
    healthcheck
    """
    return flask.jsonify({"msg": "pong"})
