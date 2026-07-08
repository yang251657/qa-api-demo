# 所有和登录相关的 例如登录/登出， service 只调用client发请求，不做任何断言，断言交给测试用例去做
from clients.http_client import HttpClient
from config.settings import BASE_URL


class AuthService:
    def __init__(self):
        self.client = HttpClient(BASE_URL)

    
    def login(self, email, password):
        payload = {"email": email, "password": password}
        return self.client.post("/login", json=payload)
    

    

    