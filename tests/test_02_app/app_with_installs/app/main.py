import sys

from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    return f"Hello World from Nginx uWSGI Python {version} app in a Docker container"
