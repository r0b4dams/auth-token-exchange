"""server"""

from flask import Blueprint, Flask
from flask_cors import CORS
from gunicorn.app.base import BaseApplication


class Server(BaseApplication):
    """
    Top-level class managing the application
    """

    def __init__(self, name: str, config: dict[str, str], blueprints: list[Blueprint]):
        self.app = Flask(name)
        self.config = config
        self.register_blueprints(blueprints)
        CORS(self.app, supports_credentials=True)
        super().__init__()

    def init(self, *_):
        pass

    def listen(self):
        """
        start the server and run forever
        uses Gunicorn in production, else starts Flask dev server
        """
        if self.config["mode"] == "production":
            self.run()
        else:
            self.app.run(debug=True, host=self.config["host"], port=self.config["port"])

    def load(self):
        """
        used by BaseApplication to access the Flask instance
        """
        return self.app

    def load_config(self):
        """
        filter valid Gunicorn properties and set config on BaseApplication
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
        add blueprints to the Flask app
        """
        for blueprint in blueprints:
            self.app.register_blueprint(blueprint)
