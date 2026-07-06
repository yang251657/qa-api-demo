
# 所有和登录相关的 例如登录/登出
from clients.http_client import HttpClient
from config.settings import BASE_URL

# from config.settings import BASE_URL, DEFAULT_HEADERS
# from utils.logger import get_logger

# logger = get_logger(__name__)

class AuthService:
    def __init__(self):
        self.client = HttpClient(BASE_URL)

    
    def login(self, email, password):
        payload = {"email": email, "password": password}
        return self.client.post("/login", json=payload)
    

    # def login(self, email, password):
    #     url = f"{BASE_URL}/login"
    #     payload = {"email": email, "password": password}
    #     response = requests.post(url, json=payload, headers=DEFAULT_HEADERS)
    #     logger.info(f"响应 <- {response.status_code} | body={response.text}")
    #     return response
    

    