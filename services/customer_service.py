from clients.http_client import HttpClient
from config.settings import BASE_URL
from services.auth_service import AuthService


class CustomerService:
    """
    模拟CRM系统的客户管理接口。
    token 通过构造函数传入；如果请求返回401(token失效)，
    会自动重新登录一次并重试原请求一次。
    """

    def __init__(self, token: str = None):
        self.client = HttpClient(BASE_URL)
        self.token = token

    def _auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def _refresh_token(self):
        """token失效时，重新登录拿新token"""
        auth = AuthService()
        response = auth.login("eve.holt@reqres.in", "cityslicka")
        self.token = response.json().get("token")

    def get_customer(self, customer_id):
        response = self.client.get(f"/users/{customer_id}", extra_headers=self._auth_headers())

        if response.status_code == 401:
            self._refresh_token()
            response = self.client.get(f"/users/{customer_id}", extra_headers=self._auth_headers())

        return response

    def get_customer_list(self, page=1):
        response = self.client.get("/users", params={"page": page}, extra_headers=self._auth_headers())

        if response.status_code == 401:
            self._refresh_token()
            response = self.client.get("/users", params={"page": page}, extra_headers=self._auth_headers())

        return response