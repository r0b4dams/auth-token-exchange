import os
import multiprocessing

mode = os.environ.get("MODE", "development")
host = os.environ.get("HOST", "localhost")
port = os.environ.get("PORT", "9000")


def number_of_workers():
    return multiprocessing.cpu_count()


config = {
    "mode": mode,
    "host": host,
    "port": port,
    'bind': '%s:%s' % (host, port),
    'workers': number_of_workers(),
}
