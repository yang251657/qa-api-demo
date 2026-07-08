# import sys
# import os
import pytest
from utils.assertions import assert_status_code, assert_json_has_keys
from conftest import load_cases_by_module


login_cases = load_cases_by_module("test_data.yaml", "login")

login_params = [
    pytest.param(case, marks=getattr(pytest.mark, case["mark"]), id=case["case_name"])
    for case in login_cases
]

@pytest.mark.smoke
def test_login_success(auth_service):   # 直接把 fixture 名字写成函数参数
    response = auth_service.login(
        "eve.holt@reqres.in",
        "cityslicka"
    )
    assert_status_code(response, 200)
    assert_json_has_keys(response, ["token"])


@pytest.mark.parametrize("case",login_params)
def test_login_scenarios(auth_service, case):
    response = auth_service.login(case["data"]["email"], case["data"]["password"])
    assert_status_code(response, case["expected"]["status_code"])