from authexchange.utils import b64


def test_encode():
    decoded = "Hello, World!"
    encoded = "SGVsbG8sIFdvcmxkIQ=="
    assert b64.encode(decoded) == encoded


def test_decode():
    decoded = "Hello, World!"
    encoded = "SGVsbG8sIFdvcmxkIQ=="
    assert b64.decode(encoded) == decoded
