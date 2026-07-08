import pytest
from services.customer_service import CustomerService
from conftest import load_cases_by_module

customer_cases = load_cases_by_module("test_data.yaml", "customer")

customer_params = [
    pytest.param(case, marks=getattr(pytest.mark, case["mark"]), id=case["case_name"])
    for case in customer_cases
]

@pytest.mark.smoke
def test_get_customer_success(customer_service):
    response = customer_service.get_customer(2)
    assert response.status_code == 200
    assert "data" in response.json()


@pytest.mark.parametrize("case", customer_params)
def test_get_customer_scenarios(customer_service, case):
    response = customer_service.get_customer(case["data"]["customer_id"])
    assert response.status_code == case["expected"]["status_code"]


@pytest.mark.regression
def test_get_customer_list(customer_service):
    response = customer_service.get_customer_list(page=1)
    assert response.status_code == 200
    assert "data" in response.json()


@pytest.mark.regression
def test_get_customer_with_expired_token_auto_retry():
    customer = CustomerService(token="expired_invalid_token")
    response = customer.get_customer(2)
    assert response.status_code == 200

    