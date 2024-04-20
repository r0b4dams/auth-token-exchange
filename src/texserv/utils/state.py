from urllib.parse import urlencode
from flask import Request
from texserv.utils import b64


def generate_redirect_url(req: Request) -> str:
    encoded_uri, state, *_ = req.args.get("state").split(":")
    redirect_uri = b64.decode(encoded_uri)
    query = urlencode(
        {
            "state": state,
            "user_state": req.args.get("state"),
            "locale": req.args.get("state"),
        }
    )
    return "".join([redirect_uri, "?", query])


def push_redirect_url(redirect_uri: str, state: str) -> str:
    encoded_uri = b64.encode(redirect_uri)
    return ":".join([encoded_uri, state])
