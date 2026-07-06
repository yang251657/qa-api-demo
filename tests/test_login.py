import sys
import os
import pytest
from utils.assertions import assert_status_code, assert_json_has_keys
from conftest import load_yaml_data

login_cases = load_yaml_data("login_data.yaml")

def test_login_success(auth_service):   # 直接把 fixture 名字写成函数参数
    response = auth_service.login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert_status_code(response, 200)
    assert_json_has_keys(response, ["token"])



@pytest.mark.parametrize(
    "case",
    login_cases,
    ids=[case["case_name"] for case in login_cases],
)
def test_login_scenarios(auth_service, case):
    response = auth_service.login(case["email"], case["password"])
    assert_status_code(response, case["expected_status"])