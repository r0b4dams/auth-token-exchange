import base64

ENCODING = "ascii"


def encode(string: str) -> str:
    str_bytes = string.encode(ENCODING)
    b64_bytes = base64.b64encode(str_bytes)
    return b64_bytes.decode(ENCODING)


def decode(string: str) -> str:
    b64_bytes = string.encode(ENCODING)
    str_bytes = base64.b64decode(b64_bytes)
    return str_bytes.decode(ENCODING)
