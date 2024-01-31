from server import Server
from config import config
from routes import blueprints


Server(config, blueprints).listen()
