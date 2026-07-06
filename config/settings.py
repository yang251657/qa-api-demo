import os
from dotenv import load_dotenv

load_dotenv()  # 读取根目录的 .env 文件

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("API_KEY")


#  api key是请求头里得key  确保访问服务器
# 配置（URL / ENV / TOKEN）

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}


DEFAULT_TIMEOUT = 10