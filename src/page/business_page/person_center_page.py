# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class PersonCenterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/person_center_element.yaml"

    # 定位个人中心返回按钮
    def get_person_center_back(self):
        logging.info("定位个人中心返回按钮")
        person_center_back = self.locate_element(self.file_path, "person_center_back_btn")
        return person_center_back

    # 定位个人主页入口
    def get_person_center_entrance(self):
        logging.info("定位个人主页入口")
        person_center_entrance = self.locate_element(self.file_path, "person_center_entrance")
        return person_center_entrance