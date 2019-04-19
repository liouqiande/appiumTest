# -*- coding: utf-8 -*-
import pytest
from allure import MASTER_HELPER as allure
import time
from common.init_driver import init_driver
from handle.login_handle import LoginHandle


@allure.feature("登陆")
class TestLogin(object):

    @classmethod
    def setup_class(cls):
        cls.driver = init_driver()

    # 正常登陆

    @allure.story("正常登陆")
    def test_login(self):
        login_handle = LoginHandle(TestLogin.driver)
        login_handle.login_main("xxxx", "xxxx")
        # 校验是否登陆成功进入首页
        assert login_handle.get_homepage_tab_text() == "首页"


