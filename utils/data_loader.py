#专门负责把测试数据从文件里读出来的人

import os
import yaml


def load_yaml_data(filename: str):
    """读取 data/ 目录下的yaml文件，返回解析后的原始数据结构"""
    # 定位到项目根目录下的data文件夹
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(project_root, "data", filename)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_cases_by_module(filename: str, module: str):
    """从指定的yaml文件里，读取指定模块的测试用例列表"""
    all_data = load_yaml_data(filename)
    all_cases = all_data["cases"]
    return [case for case in all_cases if case["module"] == module]