import flask
import requests

import authexchange.config as cfg


def handle_user():
    req = flask.request
    access_token = req.cookies.get("app.at")

    if not access_token:
        res = flask.jsonify({"error": "Access token is missing"})
        res.status_code = 401
        return res

    url = "".join([cfg.FUSIONAUTH_NET_URL, "/oauth2/userinfo"])
    res = requests.get(
        url,
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=10,
    )
    data = res.json()

    return flask.jsonify(data)
