from flask import request, jsonify
from requests import get
from config import FUSIONAUTH_BASE_URL


def handle_user():
    access_token = request.cookies.get("app.at")

    if not access_token:
        response = jsonify({"error": "no access token found"})
        response.status_code = 401
        return response

    url = "".join([FUSIONAUTH_BASE_URL, "/oauth2/userinfo"])
    data = get(url, headers={
        "Authorization": "Bearer %s" % access_token
    }).json()
    return jsonify(data)
