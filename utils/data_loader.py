"""
测试数据加载工具。

企业标准做法：conftest.py只负责fixture和pytest hooks，
不承担"业务工具函数"的职责，工具函数应该放在独立的utils模块里，
方便被非fixture场景复用，职责边界更清晰。
"""
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
    """
    从统一的test_data.yaml里，按module字段筛选出属于某个业务模块的用例数据。
    """
    all_data = load_yaml_data(filename)
    all_cases = all_data["cases"]
    return [case for case in all_cases if case["module"] == module]