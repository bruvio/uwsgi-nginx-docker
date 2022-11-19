import sys


def application(env, start_response):
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = f"Hello World from Nginx uWSGI Python {version} app in a Docker container"

    return [message.encode("utf-8")]
