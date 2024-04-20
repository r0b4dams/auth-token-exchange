from urllib.parse import urlencode
from time import time
from flask import request, make_response
from requests import post
from texserv.config import (
    FUSIONAUTH_BASE_URL,
    FUSIONAUTH_CLIENT_ID,
    FUSIONAUTH_CLIENT_SECRET,
)


def handle_refresh():
    """
    TODO: doc str
    """
    refresh_token = request.cookies.get("app.rt")

    if not refresh_token:
        raise Exception("no refresh token found")

    response = post(
        url="".join([FUSIONAUTH_BASE_URL, "/oauth2/token"]),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=urlencode(
            {
                "grant_type": "refresh_token",
                "refresh_token": request.cookies.get("app.rt"),
                "access_token": request.cookies.get("app.at"),
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
        raise Exception("access token or refresh token missing")

    response = make_response()
    response.status_code = 204

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

    # save tokens
    response.set_cookie(
        "app.at", access_token, httponly=True, secure=True, samesite="lax"
    )
    response.set_cookie(
        "app.rt", refresh_token, httponly=True, secure=True, samesite="lax"
    )
    response.set_cookie(
        "app.idt", id_token, httponly=False, secure=True, samesite="lax"
    )

    # cleanup
    response.delete_cookie("code_verifier")

    return response
