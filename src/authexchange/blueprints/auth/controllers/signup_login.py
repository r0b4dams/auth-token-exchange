import urllib.parse

import flask
import pkce

from authexchange.utils import state
import authexchange.config as cfg


def handle_signup():
    return handle_signup_login("register")


def handle_login():
    return handle_signup_login("authorize")


def handle_signup_login(authtype: str):
    """
    Except for the url, the process for signup and login are identical

    Args
        authtype: Either 'register' to signup or 'authorize' to login

    Returns
        A Flask Response that redirects to the corresponding FusionAuth page

    """
    req = flask.request
    new_state = state.push_redirect_url(
        req.args.get("redirect_uri", default=req.host_url),
        req.args.get("state", default=""),
    )
    code_verifier, code_challenge = pkce.generate_pkce_pair()
    redirect_uri = "".join(
        [
            req.scheme,
            "://",
            req.host,
            "/auth/callback",
        ]
    )
    query = urllib.parse.urlencode(
        {
            "response_type": "code",
            "scope": "openid offline_access",
            "client_id": req.args.get("client_id"),
            "state": new_state,
            "redirect_uri": redirect_uri,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
        }
    )
    redirect_url = "".join(
        [
            cfg.FUSIONAUTH_BASE_URL,
            f"/oauth2/{authtype}",
            "?",
            query,
        ]
    )
    res = flask.redirect(
        redirect_url,
        code=302,
    )
    res.set_cookie(
        "code_verifier",
        code_verifier,
        secure=True,
        httponly=True,
        samesite="lax",
    )
    return res
