"""
项目全局配置文件。

支持多环境切换：通过系统环境变量 ENV 决定读取哪一份 .env 文件
(例如 ENV=test1 时读取 .env.test1)。默认使用 test1 环境。

用法：
    Windows PowerShell:  $env:ENV="test2"; pytest
    Linux/Mac:           ENV=test2 pytest
"""


import os
from dotenv import load_dotenv

current_env = os.getenv("ENV", "test1")   # 默认用 test1

env_file = f".env.{current_env}"
load_dotenv(env_file)  # 读取 .env.test1 或 .env.test2 这个文件

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")  # 从刚才读进来的文件内容里，拿API_KEY这个值

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}

DEFAULT_TIMEOUT = 10