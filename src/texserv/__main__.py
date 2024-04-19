#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
texserv
"""

import argparse
from .server import Texserv
from .blueprints import app_blueprints
from .config import app_config
from . import __version__, __app_name__


def cli():
    """
    A CLI to run the server
    """
    parser = argparse.ArgumentParser(
        prog=__app_name__,
        description="A server to handle the OAuth token exchange build with Flask",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(title="command")

    run_cmd = subparsers.add_parser("run")
    run_group = run_cmd.add_mutually_exclusive_group()
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
    run_cmd.set_defaults(func=run)

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
        app_config["mode"] = "production"
    Texserv(__app_name__, app_config, app_blueprints).listen()
