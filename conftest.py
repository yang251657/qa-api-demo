"""
全局pytest配置文件。

作用：
1. pytest运行时自动识别本文件所在目录为项目根目录，加入模块搜索路径。
2. 定义跨测试文件共用的fixture(auth_service、auth_token、customer_service)。

数据加载相关的工具函数，见 utils/data_loader.py
"""
import pytest

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