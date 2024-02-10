#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import project_data
from server import Server
from config import config
from blueprints import blueprints


Server(project_data["app_name"], config, blueprints).listen()
