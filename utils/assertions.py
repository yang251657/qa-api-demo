def assert_status_code(response, expected_code: int):
    actual_code = response.status_code
    assert actual_code == expected_code, (
        f"接口 {response.request.method} {response.request.url} "
        f"期望状态码 {expected_code}，实际返回 {actual_code}，"
        f"响应内容：{response.text}"
    )


def assert_json_has_keys(response, keys: list):
    body = response.json()
    missing = [k for k in keys if k not in body]
    assert not missing, f"响应中缺少字段：{missing}，实际响应：{body}"
    


def assert_json_contains(response, expected_subset: dict, path: str = None):
    """
    断言响应JSON里包含expected_subset指定的键值对。
    path: 可选，指定要在响应体的哪个嵌套字段下查找，比如 "data"
    """
    body = response.json()
    target = body.get(path, {}) if path else body

    for key, expected_value in expected_subset.items():
        actual_value = target.get(key)
        assert actual_value == expected_value, (
            f"字段 {key} 期望值 {expected_value}，实际值 {actual_value}，完整响应：{body}"
        )
        


def assert_schema(response, schema: dict):

    import jsonschema
    body = response.json()
    try:
        jsonschema.validate(instance=body, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        assert False, f"响应结构不符合schema预期：{e.message}，完整响应：{body}"



def assert_response(
    response,
    *,
    expected_status: int = None,
    expected_keys: list = None,
    expected_values: dict = None,
    schema: dict = None,
    path: str = None,
):
   
    if expected_status is not None:
        assert_status_code(response, expected_status)

    if expected_keys is not None:
        assert_json_has_keys(response, expected_keys)

    if expected_values is not None:
        assert_json_contains(response, expected_values, path=path)

    if schema is not None:
        assert_schema(response, schema)