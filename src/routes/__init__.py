from routes.ping import ping_blueprint
from routes.auth import auth_blueprint

blueprints = [
    ping_blueprint,
    auth_blueprint
]
