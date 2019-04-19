# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class MsgCenterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/msg_center_element.yaml"

    # 定位消息中心返回按钮
    def get_msg_center_back(self):
        logging.info("定位消息中心返回按钮")
        msg_center_back_btn = self.locate_element(self.file_path, "msg_center_back_btn")
        return msg_center_back_btn

    # 定位消息中心title
    def get_msg_center_title(self):
        logging.info("定位消息中心title")
        msg_center_title = self.locate_element(self.file_path, "msg_center_title")
        return msg_center_title