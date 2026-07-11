from clients.http_client import HttpClient
from config.settings import BASE_URL
from services.auth_service import AuthService


class CustomerService:

    def __init__(self, token: str = None):
        self.client = HttpClient(BASE_URL)
        self.token = token

    def _auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def _refresh_token(self):
        auth = AuthService()
        response = auth.login("alice2@test.com", "pass123")
        self.token = response.json().get("token")

    def _post_with_retry(self, path: str, json: dict = None):
        response = self.client.post(path, json=json, extra_headers=self._auth_headers())

        if response.status_code == 401:
            self._refresh_token()
            response = self.client.post(path, json=json, extra_headers=self._auth_headers())

        return response

    def create_customer(self, name: str, email: str, phone: str = "", company: str = ""):
        payload = {"name": name, "email": email, "phone": phone, "company": company}
        return self._post_with_retry("/customer", json=payload)