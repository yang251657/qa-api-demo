# 放fixture 、hook等，仅提供能力

# 常见 fixture：
# login / token
# client 初始化
# service 初始化
# headers
# test user
# test data setup
import pytest
import uuid

from services.auth_service import AuthService
from services.customer_service import CustomerService


@pytest.fixture
def auth_service():
    return AuthService()


@pytest.fixture(scope="session")
def auth_token():
    auth = AuthService()
    response = auth.login("eve.holt@reqres.in", "cityslicka")
    return response.json().get("token")


@pytest.fixture
def customer_service(auth_token):
    return CustomerService(token=auth_token)



@pytest.fixture
def temp_customer(customer_service):
    """
    创建一个测试专用的临时客户，用唯一标识避免和其他测试冲突。
    测试结束后自动清理，不管测试是成功还是失败都会执行清理(yield机制保证)。
    """
    unique_name = f"test_customer_{uuid.uuid4().hex[:8]}"
    response = customer_service.create_customer(name=unique_name)
    customer_id = response.json().get("id")

    yield {"id": customer_id, "name": unique_name}

    # 测试结束后，不管上面的用例是pass还是fail，这一行都会执行
    customer_service.delete_customer(customer_id)