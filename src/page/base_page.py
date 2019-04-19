# -*- coding: utf-8 -*-
import os
from appium.webdriver.webdriver import WebDriver
from util.oper_yaml import OperYaml
import logging
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver: WebDriver = driver

    # 定位元素
    def locate_element(self, file_path, ele_name):
        oper_yaml = OperYaml()
        ele_by = oper_yaml.get_ele_info(ele_name, file_path)[0]
        ele_value = oper_yaml.get_ele_info(ele_name, file_path)[1]
        element = None
        try:
            if ele_by == "ID":
                element = self.driver.find_element_by_id(ele_value)
            elif ele_by == "ClassName":
                element = self.driver.find_element_by_class_name(ele_value)
            elif ele_by == "XPath":
                element = self.driver.find_element_by_xpath(ele_value)
            elif ele_by == "Text":
                element = self.driver.find_element_by_partial_link_text(ele_value)
            else:
                element = self.driver.find_element_by_android_uiautomator(ele_value)
        except:
            logging.info("没有找到{}元素".format(str(ele_name)))
        return element

    # 获取page_source
    def get_page_source(self):
        print(self.driver.page_source())

    # 滑动按钮
    def slide_button(self):
        win_size = self.driver.get_window_size()
        x_start = win_size['width'] * 0.15
        y_start = win_size['height'] * 0.5
        x_end = win_size['height'] * 0.85
        self.driver.swipe(x_start, y_start, x_end, y_start, 1000)

    # 获取当前时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 截图
    def getScreenShot(self, module):
        time = self.getTime()
        # image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        image_file = 'D:/pyproject/DidiDriverTestProject/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)