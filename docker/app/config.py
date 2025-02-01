import os


class Config:
    """Base configuration class."""

    SECRET_KEY = os.getenv("APP_SECRET_KEY", "default-secret")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


config = Config()
