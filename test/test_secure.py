import os
import pytest
from utils.secure import get_secret

def test_get_secret_env(monkeypatch):
    """Test fetching secret from environment variable."""
    monkeypatch.setenv("DEPLOY_SECRET", "super-secret-key")
    assert get_secret() == "super-secret-key"

def test_get_secret_default():
    """Test fallback when no secret is set."""
    assert get_secret() == "default_secret"
