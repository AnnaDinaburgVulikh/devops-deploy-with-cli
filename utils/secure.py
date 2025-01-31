import os

def get_secret():
    """Retrieve secret from environment variable securely."""
    return os.getenv("DEPLOY_SECRET", "default_secret")
