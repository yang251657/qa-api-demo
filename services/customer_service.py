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
        response = auth.login("eve.holt@reqres.in", "cityslicka")
        self.token = response.json().get("token")

    def _get_with_retry(self, path: str, params: dict = None):
        response = self.client.get(path, params=params, extra_headers=self._auth_headers())

        if response.status_code == 401:
            self._refresh_token()
            response = self.client.get(path, params=params, extra_headers=self._auth_headers())

        return response

    def get_customer(self, customer_id):
        return self._get_with_retry(f"/users/{customer_id}")

    def get_customer_list(self, page: int = 1):
        return self._get_with_retry("/users", params={"page": page})
    

    def create_customer(self, name: str, job: str = "QA Engineer"):
        payload = {"name": name, "job": job}
        return self.client.post("/users", json=payload, extra_headers=self._auth_headers())

    def delete_customer(self, customer_id):
        return self.client.delete(f"/users/{customer_id}", extra_headers=self._auth_headers())