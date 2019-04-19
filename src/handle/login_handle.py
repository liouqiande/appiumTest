# -*- coding: utf-8 -*-
from page.business_page.login_page import LoginPage
import time
from allure import MASTER_HELPER as allure


# 登陆页面操作
class LoginHandle(object):
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    # 输入手机号码
    @allure.step("输入手机号码")
    def input_phone_num(self, phone_num):
        self.login_page.get_phone_num().send_keys(phone_num)
        return self

    # 点击同意单选框
    @allure.step("点击同意单选框")
    def click_agree_law(self):
        self.login_page.get_agree_law().click()
        return self

    # 点击下一步按钮
    @allure.step("点击下一步按钮")
    def click_next_btn(self):
        self.login_page.get_next_btn().click()
        return self

    # 输入密码
    @allure.step("输入密码")
    def input_password(self, password):
        self.login_page.get_password().send_keys(password)
        return self

    # 点击确认按钮
    @allure.step("点击确认按钮")
    def click_confirm_btn(self):
        self.login_page.get_confirm_btn().click()
        return self

    # 点击弹屏广告关闭按钮
    @allure.step("点击弹屏广告关闭按钮")
    def click_adver_close_btn(self):
        self.login_page.get_adver_close_btn().click()
        return self

    # 获取首页tab文案
    @allure.step("获取首页tab文案")
    def get_homepage_tab_text(self):
        return self.login_page.get_homepage_tab().get_attribute("text")

    # 输入手机号流程并点击下一步
    def phone_num_main(self, phone_num):
        self.input_phone_num(phone_num)
        self.click_agree_law()
        self.click_next_btn()
        return self

    # 输入密码并点击确认
    def passowrd_main(self, password):
        self.input_password(password)
        self.click_confirm_btn()
        return self

    # 登陆主流程
    def login_main(self, phone_num, password):
        # 输入手机号码、点击同意、点击下一步按钮
        self.phone_num_main(phone_num)
        # 输入密码、点击确认按钮
        self.passowrd_main(password)
        if self.login_page.get_adver_close_btn() != None:
            self.click_adver_close_btn()
        time.sleep(5)