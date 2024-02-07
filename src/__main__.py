#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import Server
from config import config
from blueprints import blueprints


Server(config, blueprints).listen()
