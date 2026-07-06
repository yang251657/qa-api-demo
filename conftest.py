import pytest
import os
import yaml

from services.auth_service import AuthService


@pytest.fixture
def auth_service():
    return AuthService()


def load_yaml_data(filename: str):
    path = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    