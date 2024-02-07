import flask

ping_blueprint = flask.Blueprint("ping", __name__, url_prefix="/ping")


@ping_blueprint.route("/", methods=["GET"], strict_slashes=False)
def ping():
    response = {
        "response": "pong",
        "status": 200
    }
    return flask.make_response(flask.jsonify(response), response["status"])
