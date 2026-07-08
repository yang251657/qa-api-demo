"""
登录接口测试用例。
"""
import pytest
from utils.assertions import assert_response
from utils.data_loader import load_cases_by_module

login_cases = load_cases_by_module("test_data.yaml", "login")

login_params = [
    pytest.param(case, marks=getattr(pytest.mark, case.get("mark", "regression")), id=case["case_name"])
    for case in login_cases
]


@pytest.mark.parametrize("case", login_params)
def test_login_scenarios(auth_service, case):
    response = auth_service.login(case["data"]["email"], case["data"]["password"])

    expected_status = case["expected"]["status_code"]
    if expected_status == 200:
        assert_response(response, expected_status=200, expected_keys=["token"])
    else:
        assert_response(response, expected_status=expected_status)