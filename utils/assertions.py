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