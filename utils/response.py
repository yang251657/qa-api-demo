"""
Response包装类。

解决的问题：直接调用 response.json() 时，如果接口返回的不是合法JSON
(比如服务挂了返回HTML错误页、网关超时返回纯文本)，会抛出让人困惑的
JSONDecodeError，掩盖了"接口本身出错"这个真实原因。

这个wrapper统一做异常兜底，让失败信息更直接。
"""


class ResponseWrapper:

    def __init__(self, response):
        self.response = response

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def text(self):
        return self.response.text

    @property
    def request(self):
        """转发原始response的request属性，保留断言报错信息的完整性"""
        return self.response.request

    def json(self):
        try:
            return self.response.json()
        except ValueError:
            return {
                "_parse_error": True,
                "_status_code": self.response.status_code,
                "_raw_text": self.response.text[:200],
            }

    def get(self, key, default=None):
        return self.json().get(key, default)