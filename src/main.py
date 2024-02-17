"""token-exchange"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from server import Server
from config import config
from blueprints import blueprints


def main():
    """
    Start the server and run forever
    """
    with open("project.json", encoding="utf-8") as data:
        project_data = json.load(data)
    app_name = f"{project_data['name']}-{project_data['version']}"
    Server(app_name, config, blueprints).listen()


if __name__ == "__main__":
    main()
