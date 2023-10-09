"""Command line entrypoint for docker2quadlet"""
import argparse
import sys
from typing import Optional

import yaml

from docker2quadlet.compose import compose_to_services


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser(
        "docker2quadlet",
        description="Convert docker commands to podman/systemd quadlet files",
    )
    parser.add_argument("compose_file", help="Some parameter")
    return parser.parse_args(arguments)


def cli(arguments: Optional[list[str]] = None):
    """Run the docker2quadlet cli"""
    if arguments is None:
        arguments = sys.argv[1:]
    args = parse_arguments(arguments)
    main(args.compose_file)


def main(compose_file):
    """Run the program's main command"""
    with open(compose_file, "r") as fd:
        svc = yaml.load(fd, Loader=yaml.Loader)
    quad_list = compose_to_services(svc)
    print(f"Got {len(quad_list)} services!")
    for service_name, service in quad_list.items():
        print(f"{'='*30} {service_name} {'='*30}")
        print(service)
