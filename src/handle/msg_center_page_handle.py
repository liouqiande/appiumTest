# -*- coding: utf-8 -*-
from page.business_page.msg_center_page import MsgCenterPage
from allure import MASTER_HELPER as allure


# 消息中心页面操作
class MsgCenterHandle(object):
    def __init__(self,driver):
        self.msg_center_page = MsgCenterPage(driver)

    # 点击消息中心页返回按钮
    @allure.step("点击消息中心页返回按钮")
    def click_msg_center_back(self):
        self.msg_center_page.get_msg_center_back().click()
        return self

    # 获取消息中心页面title
    @allure.step("获取消息中心页面title")
    def get_msg_center_text(self):
        text = self.msg_center_page.get_msg_center_title().get_attribute("text")
        return text