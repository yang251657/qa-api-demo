def test_get_customer_success(customer_service):
    response = customer_service.get_customer(2)

    assert response.status_code == 200
    assert "data" in response.json()


def test_get_customer_list(customer_service):
    response = customer_service.get_customer_list(page=1)

    assert response.status_code == 200
    assert "data" in response.json()


from services.customer_service import CustomerService


def test_get_customer_with_expired_token_auto_retry():
    """故意用一个无效token，验证401后能自动刷新重试成功"""
    customer = CustomerService(token="expired_invalid_token")
    response = customer.get_customer(2)

    assert response.status_code == 200