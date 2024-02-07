from urllib.parse import urlencode
from time import time
from requests import post
from flask import Blueprint, request, redirect, jsonify
from pkce import generate_pkce_pair
from .state import *
from config import FUSIONAUTH_BASE_URL, FUSIONAUTH_CLIENT_ID, FUSIONAUTH_CLIENT_SECRET

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    code_verifier = request.cookies.get("code_verifier")

    redirect_uri = "".join(
        [request.scheme, "://", request.host, "/auth/callback"])

    r = post(
        url="".join([FUSIONAUTH_BASE_URL, "/oauth2/token"]),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        data=urlencode({
            "grant_type": 'authorization_code',
            "code": code,
            "code_verifier": code_verifier,
            "redirect_uri": redirect_uri,
            "client_id": FUSIONAUTH_CLIENT_ID,
            "client_secret": FUSIONAUTH_CLIENT_SECRET,
        })
    )

    data = r.json()

    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    id_token = data["id_token"]
    expires_in = data["expires_in"]

    if not access_token or not refresh_token:
        raise Exception("access token or refresh token missing")

    redirect_url = state.generate_redirect_url(request)
    response = redirect(redirect_url)

    # set token expiration in a readable cookie
    time_ms = int(time() * 1000)
    expires_in_ms = int(expires_in * 1000)
    response.set_cookie("app.at_exp", str(time_ms + expires_in_ms),
                        httponly=False, secure=True, samesite='lax', max_age=expires_in_ms)

    # save tokens
    response.set_cookie("app.at", access_token,
                        httponly=True, secure=True, samesite='lax')
    response.set_cookie("app.rt", refresh_token,
                        httponly=True, secure=True, samesite='lax')
    response.set_cookie("app.idt", id_token,
                        httponly=False, secure=True, samesite='lax')

    # cleanup
    response.delete_cookie("code_verifier")

    return response


@auth_blueprint.route("/login", methods=["GET"])
def login():
    new_state = state.push_redirect_url(request.args.get(
        "redirect_uri"), request.args.get("state"))

    code_verifier, code_challenge = generate_pkce_pair()

    redirect_uri = "".join(
        [request.scheme, "://", request.host, "/auth/callback"])

    query = urlencode({
        "response_type": "code",
        "scope": "openid offline_access",
        "client_id": request.args.get("client_id"),
        "state": new_state,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    })

    redirect_url = "".join(
        [FUSIONAUTH_BASE_URL, "/oauth2/authorize", "?", query])

    response = redirect(redirect_url, code=302)
    response.set_cookie("code_verifier", code_verifier,
                        secure=True,  httponly=True, samesite="lax")

    return response


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    query = urlencode({
        "post_logout_redirect_uri": request.args.get("post_logout_redirect_uri"),
        "client_id": request.args.get("client_id"),
        "id_token_hint": request.cookies.get("app.idt")
    })
    redirect_url = "".join([FUSIONAUTH_BASE_URL, "/oauth2/logout", "?", query])
    response = redirect(redirect_url, code=302)

    for key in ["app.at", "app.at_exp", "app.rt", "app.idt"]:
        response.delete_cookie(key)

    return response


# @auth_blueprint.route("/refresh", methods=["POST"])
# def refresh():
#     return auth_controller.refresh()


@auth_blueprint.route("/register", methods=["GET"])
def register():
    new_state = state.push_redirect_url(
        request.args.get("redirect_uri"),
        request.args.get("state")
    )

    code_verifier, code_challenge = generate_pkce_pair()

    redirect_uri = "".join(
        [request.scheme, "://", request.host, "/auth/callback"])

    query = urlencode({
        "response_type": "code",
        "scope": "openid offline_access",
        "client_id": request.args.get("client_id"),
        "state": new_state,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    })

    redirect_url = "".join(
        [FUSIONAUTH_BASE_URL, "/oauth2/register", "?", query])

    response = redirect(redirect_url, code=302)

    response.set_cookie("code_verifier", code_verifier,
                        secure=True,  httponly=True,  samesite="lax")

    return response


# @auth_blueprint.route("/user", methods=["GET"])
# def user():
#     return auth_controller.user()
