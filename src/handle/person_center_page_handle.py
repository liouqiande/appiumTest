# -*- coding: utf-8 -*-
from page.business_page.person_center_page import PersonCenterPage
import time
from allure import MASTER_HELPER as allure


# 个人中心页面操作
class PersonCenterHandle(object):
    def __init__(self,driver):
        self.person_center_page = PersonCenterPage(driver)

    # 点击个人中心页返回按钮
    @allure.step("点击个人中心页返回按钮")
    def click_person_center_back(self):
        self.person_center_page.get_person_center_back().click()
        return self

    # 获取个人主页入口文案
    @allure.step("获取个人主页入口文案")
    def get_person_center_text(self):
        text = self.person_center_page.get_person_center_entrance().get_attribute("text")
        return text