import os

DEBUG = bool(os.environ.get("FLASK_DEBUG", True))
ENV = os.environ.get("FLASK_ENV", "development")
# create log files in current working directory
LOG_DIR = "."
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:////tmp/radio-chaser.db",
)
# To suppress deprecation warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False
