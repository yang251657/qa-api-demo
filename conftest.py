# 放fixture 、hook等，仅提供能力

# 常见 fixture：
# login / token
# client 初始化
# service 初始化
# headers
# test user
# test data setup
import pytest

from services.auth_service import AuthService
from services.customer_service import CustomerService


@pytest.fixture
def auth_service():
    return AuthService()


@pytest.fixture(scope="session")
def auth_token():
    auth = AuthService()
    response = auth.login("clouduser@test.com", "cloudpass123")
    return response.json().get("token")


@pytest.fixture
def customer_service(auth_token):
    return CustomerService(token=auth_token)