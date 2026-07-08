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
    

def load_cases_by_module(filename: str, module: str):
    """
    从统一的test_data.yaml里，按module筛选出属于某个业务模块的用例数据
    """
    all_data = load_yaml_data(filename)
    all_cases = all_data["cases"]
    return [case for case in all_cases if case["module"] == module]
