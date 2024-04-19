# pylint: disable=W0223
"""
texserv.server
"""


from flask import Blueprint, Flask
from flask_cors import CORS
from gunicorn.app.base import BaseApplication


class Texserv(BaseApplication):
    """
    TODO: doc str
    """

    def __init__(self, name: str, config: dict[str, str], blueprints: list[Blueprint]):
        self.app = Flask(name)
        self.config = config
        self.register_blueprints(blueprints)
        CORS(self.app, supports_credentials=True)
        super().__init__()

    def listen(self):
        """
        TODO: doc str
        """
        if self.config["mode"] == "production":
            self.run()
        else:
            self.app.run(debug=True, host=self.config["host"], port=self.config["port"])

    def load(self):
        """
        TODO: doc str
        """
        return self.app

    def load_config(self):
        """
        TODO: doc str
        """
        gunicorn_config = {
            key.lower(): value
            for key, value in self.config.items()
            if key in self.cfg.settings and value is not None
        }

        for key, value in gunicorn_config.items():
            self.cfg.set(key, value)

    def register_blueprints(self, blueprints: list[Blueprint]):
        """
        TODO: doc str
        """
        for blueprint in blueprints:
            self.app.register_blueprint(blueprint)
