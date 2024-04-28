#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from . import (
    __name__ as app_name,
    __version__,
    server,
    blueprints,
    config,
)


def cli():
    """
    texserv [-h] [-v] {run} ...

    A server to handle the OAuth token exchange with FusionAuth.

    [options]:
    -h, --help     show this help message and exit
    -v, --version  show program's version number and exit

    {commands}:
        run [-h] (-d | -p)  start the server and listen forever
            -h, --help      show this help message and exit
            -d, --dev       run the app using Flask's dev server
            -p, --prod      run the server for production with Gunicorn
    """
    parser = argparse.ArgumentParser(
        prog=app_name,
        description="App to handle the OAuth token exchange with FusionAuth.",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s v{__version__}",
    )

    subparsers = parser.add_subparsers(
        title="commands",
        help="command help",
    )

    run_cmd = subparsers.add_parser(
        "run",
        description="start the server and run forever",
        help="Runs the server",
    )
    run_group = run_cmd.add_mutually_exclusive_group(
        required=True,
    )
    run_group.add_argument(
        "-d",
        "--dev",
        action="store_true",
        help="Run the server in development using Flask's debug mode",
    )
    run_group.add_argument(
        "-p",
        "--prod",
        action="store_true",
        help="Run the server for production with Gunicorn",
    )
    run_cmd.set_defaults(
        func=run,
    )

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


def run(args: argparse.Namespace):
    """
    Start the server and run forever
    """
    if args.prod:
        config.app_config["mode"] = "production"

    app = server.ExchangeServer(
        app_name,
        config.app_config,
        blueprints.app_blueprints,
    )

    app.listen()
