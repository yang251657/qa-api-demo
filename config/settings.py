import os
from dotenv import load_dotenv

current_env = os.getenv("ENV", "test1")   # 默认用 test1

env_file = f".env.{current_env}"
load_dotenv(env_file)

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}

DEFAULT_TIMEOUT = 10