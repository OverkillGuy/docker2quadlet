"""Replace a docker-compose file with quadlet"""


from jinja2 import Environment, PackageLoader, select_autoescape

JINJA_ENV = Environment(
    loader=PackageLoader("docker2quadlet"),
    autoescape=select_autoescape(),
    trim_blocks=True,
)


def service_to_quadlet(svc: dict, svc_name: str) -> str:
    """Turn a single service to a quadlet"""
    svc_template = JINJA_ENV.get_template("service.j2")
    return svc_template.render(svc=svc, svc_name=svc_name)


def compose_to_services(compose_file: dict) -> dict[str, str]:
    """Iterate over all the services of a compose file"""
    acc = {}
    for svc_name, svc in compose_file["services"].items():
        quadlet = service_to_quadlet(svc, svc_name)
        acc[f"{svc_name}.container"] = quadlet
    return acc
