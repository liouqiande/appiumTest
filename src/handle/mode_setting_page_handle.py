# -*- coding: utf-8 -*-
from page.business_page.mode_setting_page import ModeSettingPage
from allure import MASTER_HELPER as allure


# 模式设置页面操作
class ModeSettingHandle(object):
    def __init__(self,driver):
        self.mode_setting_page = ModeSettingPage(driver)

    # 点击模式设置页面关闭按钮
    @allure.step("点击模式设置页面关闭按钮")
    def click_mode_setting_back(self):
        self.mode_setting_page.get_mode_setting_back().click()
        return self

    # 获取模式设置页面title
    @allure.step("获取模式设置页面title")
    def get_mode_setting_title_text(self):
        text = self.mode_setting_page.get_mode_setting_title().get_attribute("text")
        return text

    # 点击保存设置按钮
    @allure.step("点击保存设置按钮")
    def click_mode_setting_save_btn(self):
        self.mode_setting_page.get_mode_setting_save_btn().click()
        return self