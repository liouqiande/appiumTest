# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class ModeSettingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/mode_setting_element.yaml"

    # 定位关闭按钮
    def get_mode_setting_back(self):
        logging.info("定位关闭按钮")
        mode_setting_back = self.locate_element(self.file_path, "mode_setting_back")
        return mode_setting_back

    # 定位模式设置页面title
    def get_mode_setting_title(self):
        logging.info("定位模式设置页面title")
        mode_setting_title = self.locate_element(self.file_path, "mode_setting_title")
        return mode_setting_title

    # 定位保存设置按钮
    def get_mode_setting_save_btn(self):
        logging.info("定位保存设置按钮")
        mode_setting_save_btn = self.locate_element(self.file_path, "mode_setting_save_btn")
        return mode_setting_save_btn