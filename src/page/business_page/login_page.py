# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/login_element.yaml"

    # 定位手机号输入框
    def get_phone_num(self):
        logging.info("定位手机号输入框")
        phone_num = self.locate_element(self.file_path, "phone_num")
        return phone_num

    # 定位手机号输入框
    def get_other_phone_num(self):
        logging.info("定位手机号已经不再使用")
        other_phone_num = self.locate_element(self.file_path, "other_phone_num")
        return other_phone_num

    # 定位同意单选框
    def get_agree_law(self):
        logging.info("定位同意单选框")
        agree_law = self.locate_element(self.file_path, "agree_law")
        return agree_law

    # 定位《法律条款与平台规则》
    def get_law(self):
        logging.info("定位同意单选框")
        law = self.locate_element(self.file_path, "law")
        return law

    # 定位下一步按钮
    def get_next_btn(self):
        logging.info("定位下一步按钮")
        next_btn = self.locate_element(self.file_path, "next_btn")
        return next_btn

    # 定位密码输入框
    def get_password(self):
        logging.info("定位密码输入框")
        password = self.locate_element(self.file_path, "password")
        return password

    # 定位确认按钮
    def get_confirm_btn(self):
        logging.info("定位确认按钮")
        confirm_btn = self.locate_element(self.file_path, "confirm_btn")
        return confirm_btn

    # 定位首页tab
    def get_homepage_tab(self):
        logging.info("定位首页tab")
        homepage_tab = self.locate_element(self.file_path, "homepage_tab")
        return homepage_tab

    # 定位弹屏广告关闭按钮
    def get_adver_close_btn(self):
        logging.info("定位弹屏广告关闭按钮")
        close_btn = self.locate_element(self.file_path, "close_btn")
        return close_btn