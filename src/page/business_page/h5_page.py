# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class H5Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/h5_page_element.yaml"

    # 定位h5页面返回按钮
    def get_h5_back_btn(self):
        logging.info("定位h5页面返回按钮")
        h5_back_btn = self.locate_element(self.file_path, "h5_back_btn")
        return h5_back_btn

    # 定位小桔车服行车服务按钮
    def get_car_life_buttom_btn(self):
        logging.info("定位小桔车服行车服务按钮")
        car_life_buttom_btn = self.locate_element(self.file_path, "car_life_buttom_btn")
        return car_life_buttom_btn

    # 定位h5页面title
    def get_h5_page_title(self):
        logging.info("定位h5页面title")
        h5_page_title = self.locate_element(self.file_path, "h5_page_title")
        return h5_page_title