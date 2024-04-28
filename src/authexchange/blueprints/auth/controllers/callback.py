import time
import urllib.parse

import flask
import requests

from authexchange.utils import state
import authexchange.config as cfg


def handle_callback():
    req = flask.request
    redirect_uri = "".join([req.scheme, "://", req.host, "/auth/callback"])

    fusionauth_res = requests.post(
        url="".join([cfg.FUSIONAUTH_NET_URL, "/oauth2/token"]),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=urllib.parse.urlencode(
            {
                "grant_type": "authorization_code",
                "code": req.args.get("code"),
                "code_verifier": req.cookies.get("code_verifier"),
                "redirect_uri": redirect_uri,
                "client_id": cfg.FUSIONAUTH_CLIENT_ID,
                "client_secret": cfg.FUSIONAUTH_CLIENT_SECRET,
            }
        ),
        timeout=10,
    )
    data = fusionauth_res.json()

    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    id_token = data["id_token"]
    expires_in = data["expires_in"]

    if not access_token or not refresh_token:
        res = flask.jsonify(
            {"error": "Either refresh token or access token is missing"},
        )
        res.status_code = 503
        return res

    user_state = req.args.get("state", default="")
    redirect_url = state.generate_redirect_url(user_state)
    res = flask.redirect(redirect_url)

    # set token expiration in a readable cookie
    time_ms = int(time.time() * 1000)
    expires_in_ms = int(expires_in * 1000)
    res.set_cookie(
        "app.at_exp",
        str(time_ms + expires_in_ms),
        httponly=False,
        secure=True,
        samesite="lax",
        max_age=expires_in_ms,
    )
    res.set_cookie(
        "app.idt",
        id_token,
        httponly=False,
        secure=True,
        samesite="lax",
    )
    res.set_cookie(
        "app.at",
        access_token,
        httponly=True,
        secure=True,
        samesite="lax",
    )
    res.set_cookie(
        "app.rt",
        refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
    )

    # clean up cookie set in login/register
    res.delete_cookie("code_verifier")

    return res
