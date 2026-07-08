import os
from dotenv import load_dotenv

# ===== 1. 选择环境 =====
# ENV=test1 / test2，默认test1
current_env = os.getenv("ENV", "test1")

# 加载对应环境文件
env_file = f".env.{current_env}"
load_dotenv(env_file)


# ===== 2. 基础配置 =====
BASE_URL = os.getenv("BASE_URL")

# 鉴权key
API_KEY = os.getenv("API_KEY")


# ===== 3. 默认请求头 =====
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}


# ===== 4. 超时设置 =====
DEFAULT_TIMEOUT = 10