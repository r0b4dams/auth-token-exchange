import urllib.parse

import flask

import authexchange.config as cfg

COOKIE_KEYS = [
    "app.at",
    "app.at_exp",
    "app.rt",
    "app.idt",
]


def handle_logout():
    req = flask.request
    query = urllib.parse.urlencode(
        {
            "post_logout_redirect_uri": req.args.get(
                "post_logout_redirect_uri",
            ),
            "client_id": req.args.get(
                "client_id",
            ),
            "id_token_hint": req.cookies.get(
                "app.idt",
            ),
        }
    )
    redirect_url = "".join(
        [
            cfg.FUSIONAUTH_BASE_URL,
            "/oauth2/logout",
            "?",
            query,
        ]
    )
    res = flask.redirect(redirect_url, code=302)

    for key in COOKIE_KEYS:
        res.delete_cookie(key)

    return res
