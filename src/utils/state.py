"""utils.state"""

from urllib.parse import urlencode
from flask import Request
from .b64 import encode, decode


def generate_redirect_url(req: Request) -> str:
    encoded_uri, state, *_ = req.args.get("state").split(":")
    redirect_uri = decode(encoded_uri)

    query = urlencode(
        {
            "state": state,
            "user_state": req.args.get("state"),
            "locale": req.args.get("state"),
        }
    )

    return "".join([redirect_uri, "?", query])


def push_redirect_url(redirect_uri: str, state: str) -> str:
    encoded_uri = encode(redirect_uri)
    return ":".join([encoded_uri, state])
