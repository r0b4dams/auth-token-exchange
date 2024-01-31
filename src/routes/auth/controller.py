import flask
import pkce


class AuthController:
    def __init__(self):
        pass

    def callback(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "callback"
        }
        return flask.make_response(response, status_code)

    def login(self) -> flask.Response:
        code_verifier, code_challenge = pkce.generate_pkce_pair()
        status_code = 200
        response = {
            "GET": "login",
            "code_verifier": code_verifier,
            "code_challenge": code_challenge
        }
        return flask.make_response(response, status_code)

    def logout(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "logout"
        }
        return flask.make_response(response, status_code)

    def refresh(self) -> flask.Response:
        status_code = 200
        response = {
            "POST": "refresh"
        }
        return flask.make_response(response, status_code)

    def register(self) -> flask.Response:
        code_verifier, code_challenge = pkce.generate_pkce_pair()
        status_code = 200
        response = {
            "GET": "register",
            "code_verifier": code_verifier,
            "code_challenge": code_challenge
        }
        return flask.make_response(response, status_code)

    def user(self) -> flask.Response:
        status_code = 200
        response = {
            "GET": "user"
        }
        return flask.make_response(response, status_code)
