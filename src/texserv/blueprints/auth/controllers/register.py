from urllib.parse import urlencode
from flask import request, redirect
from pkce import generate_pkce_pair
from texserv.utils import state
from texserv.config import FUSIONAUTH_BASE_URL


def handle_register():
    """
    TODO: doc str
    """
    new_state = state.push_redirect_url(
        request.args.get("redirect_uri"), request.args.get("state")
    )

    code_verifier, code_challenge = generate_pkce_pair()

    redirect_uri = "".join([request.scheme, "://", request.host, "/auth/callback"])

    query = urlencode(
        {
            "response_type": "code",
            "scope": "openid offline_access",
            "client_id": request.args.get("client_id"),
            "state": new_state,
            "redirect_uri": redirect_uri,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
        }
    )

    redirect_url = "".join([FUSIONAUTH_BASE_URL, "/oauth2/register", "?", query])

    response = redirect(redirect_url, code=302)

    response.set_cookie(
        "code_verifier", code_verifier, secure=True, httponly=True, samesite="lax"
    )

    return response
