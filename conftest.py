import pytest
import os
import yaml

from services.auth_service import AuthService
from services.customer_service import CustomerService   



@pytest.fixture
def auth_service():
    return AuthService()


@pytest.fixture(scope="session")
def auth_token():
    """
    整个测试会话只登录一次，返回token，
    给需要鉴权的接口(比如customer_service)使用。
    """
    auth = AuthService()
    response = auth.login("eve.holt@reqres.in", "cityslicka")
    return response.json().get("token")

@pytest.fixture
def customer_service(auth_token):
    """
    每次调用都拿到一个带着当前session token的customer_service实例。
    """
    return CustomerService(token=auth_token)



def load_yaml_data(filename: str):
    path = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    