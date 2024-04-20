from time import time
from urllib.parse import urlencode
from flask import request, redirect, jsonify
from requests import post
from texserv.utils import state
from texserv.config import (
    FUSIONAUTH_BASE_URL,
    FUSIONAUTH_CLIENT_ID,
    FUSIONAUTH_CLIENT_SECRET,
)


def handle_callback():
    """
    TODO: doc str
    """
    code = request.args.get("code")
    code_verifier = request.cookies.get("code_verifier")
    redirect_uri = "".join([request.scheme, "://", request.host, "/auth/callback"])

    response = post(
        url="".join([FUSIONAUTH_BASE_URL, "/oauth2/token"]),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=urlencode(
            {
                "grant_type": "authorization_code",
                "code": code,
                "code_verifier": code_verifier,
                "redirect_uri": redirect_uri,
                "client_id": FUSIONAUTH_CLIENT_ID,
                "client_secret": FUSIONAUTH_CLIENT_SECRET,
            }
        ),
        timeout=10,
    )

    data = response.json()

    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    id_token = data["id_token"]
    expires_in = data["expires_in"]

    if not access_token or not refresh_token:
        response = jsonify({"error": "Either refresh token or access token is missing"})
        response.status_code = 401
        return response

    redirect_url = state.generate_redirect_url(request)
    response = redirect(redirect_url)

    # set token expiration in a readable cookie
    time_ms = int(time() * 1000)
    expires_in_ms = int(expires_in * 1000)
    response.set_cookie(
        "app.at_exp",
        str(time_ms + expires_in_ms),
        httponly=False,
        secure=True,
        samesite="lax",
        max_age=expires_in_ms,
    )

    response.set_cookie(
        "app.at", access_token, httponly=True, secure=True, samesite="lax"
    )
    response.set_cookie(
        "app.rt", refresh_token, httponly=True, secure=True, samesite="lax"
    )
    response.set_cookie(
        "app.idt", id_token, httponly=False, secure=True, samesite="lax"
    )

    # clean up cookie set in login/register
    response.delete_cookie("code_verifier")

    return response
