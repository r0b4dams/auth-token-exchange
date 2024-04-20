import flask
from gunicorn.app import base
from src.texserv import server


def test_server_init():
    config = {"mode": "TEST"}
    s = server.Texserv("test_server", config, None)
    assert isinstance(s, base.BaseApplication)
    assert isinstance(s._app, flask.Flask)
    assert s._config == config
