# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class HotMapPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/hot_map_element.yaml"

    # 定位热力图返回按钮
    def get_hotmap_back(self):
        logging.info("定位热力图返回按钮")
        hotmap_back = self.locate_element(self.file_path, "hotmap_back")
        return hotmap_back

    # 定位热力图订单按钮
    def get_order_button(self):
        logging.info("定位热力图订单按钮")
        order_button = self.locate_element(self.file_path, "order_button")
        return order_button

    # 定位热力图奖励按钮
    def get_reward_button(self):
        logging.info("定位热力图奖励按钮")
        reward_button = self.locate_element(self.file_path, "reward_button")
        return reward_button