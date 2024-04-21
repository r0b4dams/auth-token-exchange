from authexchange.utils import b64


def generate_redirect_url(state: str) -> str:
    encoded_uri, *_ = state.split(":")
    redirect_uri = b64.decode(encoded_uri)
    return redirect_uri


def push_redirect_url(redirect_uri: str, state: str) -> str:
    encoded_uri = b64.encode(redirect_uri)
    return ":".join([encoded_uri, state])
