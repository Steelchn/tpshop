"""
主要作用放置fixture, 放置在根目录下表示作用范围是整个项目
"""

import pytest


@pytest.fixture()
def login():
    print("输入用户名密码登录成功")

@pytest.fixture()
def open_setting():
    print("打开手机设置")

    yield
    print("关闭app")
    print("关闭手机")