from . import auth, ping

app_blueprints = [
    auth.auth_blueprint,
    ping.ping_blueprint,
]
