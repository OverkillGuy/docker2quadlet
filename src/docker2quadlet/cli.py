"""Command line entrypoint for docker2quadlet"""
import argparse
import sys
from typing import Optional


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser(
        "docker2quadlet",
        description="Convert docker commands to podman/systemd quadlet files",
    )
    parser.add_argument("foo", help="Some parameter")
    return parser.parse_args(arguments)


def cli(arguments: Optional[list[str]] = None):
    """Run the docker2quadlet cli"""
    if arguments is None:
        arguments = sys.argv[1:]
    args = parse_arguments(arguments)
    main(args.foo)


def main(foo):
    """Run the program's main command"""
    print(f"Foo is: {foo}")
