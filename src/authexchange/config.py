import os

FUSIONAUTH_BASE_URL = os.environ.get("FUSIONAUTH_BASE_URL", "http://localhost:9011")
FUSIONAUTH_NET_URL = os.environ.get("FUSIONAUTH_NET_URL", FUSIONAUTH_BASE_URL)
FUSIONAUTH_CLIENT_ID = os.environ.get("FUSIONAUTH_CLIENT_ID", None)
FUSIONAUTH_CLIENT_SECRET = os.environ.get("FUSIONAUTH_CLIENT_SECRET", None)

mode = os.environ.get("MODE", "development")
host = os.environ.get("HOST", "localhost")
port = os.environ.get("PORT", "9000")
workers = os.environ.get("NUM_WORKERS", "4")

app_config = {
    "mode": mode,
    "host": host,
    "port": port,
    "bind": f"{host}:{port}",
    "workers": workers,
}
