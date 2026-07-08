import requests
from config.settings import DEFAULT_HEADERS, DEFAULT_TIMEOUT
from utils.logger import get_logger

logger = get_logger(__name__)


class HttpClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = DEFAULT_HEADERS
        self.timeout = DEFAULT_TIMEOUT

    def _full_url(self, path: str) -> str:
        return f"{self.base_url}{path}"
    
    def _merge_headers(self, extra_headers: dict = None):
        merged = dict(self.headers)
        if extra_headers:
            merged.update(extra_headers)
        return merged

    def post(self, path: str, json: dict = None):
        url = self._full_url(path)
        logger.info(f"请求 -> POST {url} | payload={json}")
        response = requests.post(url, json=json, headers=self.headers, timeout=self.timeout)
        logger.info(f"响应 <- {response.status_code} | body={response.text}")
        return response

    # def get(self, path: str, params: dict = None):
    #     url = self._full_url(path)
    #     logger.info(f"请求 -> GET {url} | params={params}")
    #     response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
    #     logger.info(f"响应 <- {response.status_code} | body={response.text}")
    #     return response
    
    def get(self, path: str, params: dict = None, extra_headers: dict = None):
        url = self._full_url(path)
        headers = self._merge_headers(extra_headers)
        logger.info(f"请求 -> GET {url} | params={params}")
        response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
        logger.info(f"响应 <- {response.status_code} | body={response.text}")
        return response