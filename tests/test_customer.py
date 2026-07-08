"""
客户管理接口测试用例(精简 demo 版)
"""
import pytest
from services.customer_service import CustomerService
from utils.data_loader import load_cases_by_module
from utils.assertions import assert_response
from schemas.customer import CUSTOMER_SCHEMA


# =========================
# 数据驱动（只保留1套）
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
# 1. 查询场景（核心）
# =========================
@pytest.mark.parametrize("case", customer_params)
def test_get_customer_scenarios(customer_service, case):

    response = customer_service.get_customer(
        case["data"]["customer_id"]
    )

    assert_response(
        response,
        expected_status=case["expected"]["status_code"],
        schema=CUSTOMER_SCHEMA if case["expected"]["status_code"] == 200 else None
    )


# =========================
# 2. 列表查询（独立API）
# =========================
def test_get_customer_list(customer_service):

    response = customer_service.get_customer_list(page=1)

    assert_response(
        response,
        expected_status=200
    )


# =========================
# 3. 异常场景（保留1个即可）
# =========================
@pytest.mark.regression
def test_get_customer_with_expired_token_auto_retry():

    customer = CustomerService(token="expired_invalid_token")

    response = customer.get_customer(2)

    assert_response(
        response,
        expected_status=200
    )


def test_create_and_verify_customer(temp_customer, customer_service):
    """验证创建的客户信息正确，数据由temp_customer fixture自动创建和清理"""
    assert temp_customer["id"] is not None
    assert "test_customer_" in temp_customer["name"]


    