"""
TODO: doc str
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import Server
from config import config
from blueprints import blueprints


def main():
    """
    TODO: doc str
    """
    Server(__name__, config, blueprints).listen()


if __name__ == "__main__":
    main()
