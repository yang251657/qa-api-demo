"""
客户管理接口测试用例(对接.NET CrmBackend)
"""
import pytest
from services.customer_service import CustomerService
from utils.data_loader import load_cases_by_module
from utils.assertions import assert_response


# =========================
# 数据驱动
# =========================
customer_cases = load_cases_by_module("test_data.yaml", "customer")

customer_params = [
    pytest.param(
        case,
        marks=getattr(pytest.mark, case.get("mark", "regression")),
        id=case["case_name"]
    )
    for case in customer_cases
]


# =========================
# 创建客户场景(数据驱动，含正向+异常)
# =========================
@pytest.mark.parametrize("case", customer_params)
def test_create_customer_scenarios(customer_service, case):
    response = customer_service.create_customer(
        name=case["data"]["name"],
        email=case["data"]["email"],
        phone=case["data"].get("phone", ""),
        company=case["data"].get("company", "")
    )

    assert_response(
        response,
        expected_status=case["expected"]["status_code"]
    )


# =========================
# token失效自动重试场景
# =========================
@pytest.mark.regression
def test_create_customer_with_expired_token_auto_retry():
    """故意用无效token，验证401后能自动刷新并重试成功"""
    customer = CustomerService(token="expired_invalid_token")
    response = customer.create_customer(
        name="Retry Test Customer",
        email="retrytest@example.com"
    )
    assert_response(response, expected_status=200)