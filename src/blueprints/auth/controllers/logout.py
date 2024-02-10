from urllib.parse import urlencode
from flask import request, redirect
from config import FUSIONAUTH_BASE_URL


def handle_logout():
    query = urlencode({
        "post_logout_redirect_uri": request.args.get("post_logout_redirect_uri"),
        "client_id": request.args.get("client_id"),
        "id_token_hint": request.cookies.get("app.idt")})

    redirect_url = "".join([FUSIONAUTH_BASE_URL, "/oauth2/logout", "?", query])

    response = redirect(redirect_url, code=302)

    for key in ["app.at", "app.at_exp", "app.rt", "app.idt"]:
        response.delete_cookie(key)

    return response
