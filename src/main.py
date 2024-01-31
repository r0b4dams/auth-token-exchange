#!/usr/bin/env python

from server import Server
from config import config
from routes import blueprints

if __name__ == "__main__":
    server = Server(config, blueprints)
    server.listen()
