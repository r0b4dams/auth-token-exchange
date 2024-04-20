from flask import Blueprint, Flask
from flask_cors import CORS
from gunicorn.app.base import BaseApplication


class Texserv(BaseApplication): # pylint: disable=abstract-method
    """
    Texserv is the top-level class managing the application

    Args:
        name:       Name of the application
        config:     Holds values from os.environ
        blueprints: A list of Flask blueprint instances
    """

    def __init__(self, name: str, config: dict[str, str], blueprints: list[Blueprint]):
        self._app = Flask(name)
        self._config = config
        self.register_blueprints(blueprints)
        CORS(self._app, supports_credentials=True)
        super().__init__()

    def listen(self):
        if self._config["mode"] == "production":
            self.run()
        else:
            self._app.run(
                debug=True,
                host=self._config["host"],
                port=self._config["port"],
            )

    def load(self):
        return self._app

    def load_config(self):
        gunicorn_config = {
            key.lower(): value
            for key, value in self._config.items()
            if key in self.cfg.settings and value is not None
        }

        for key, value in gunicorn_config.items():
            self.cfg.set(key, value)

    def register_blueprints(self, blueprints: list[Blueprint]):
        for blueprint in blueprints:
            self._app.register_blueprint(blueprint)
