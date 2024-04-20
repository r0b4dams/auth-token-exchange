from texserv.utils.state import (
    generate_redirect_url,
    push_redirect_url,
)

TEST_URL = "http://localhost:3000"
ENCODED_URL = "aHR0cDovL2xvY2FsaG9zdDozMDAw"
STATE = "b6260e09cf0e9728d132734ac676daa96c7a74aa52cbdc1b9691c7f5"


def test_generate_redirect_url():
    assert generate_redirect_url(ENCODED_URL + ":" + STATE) == TEST_URL


def test_push_redirect_url():
    assert push_redirect_url(TEST_URL, STATE) == ENCODED_URL + ":" + STATE
