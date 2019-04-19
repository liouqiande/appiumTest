# -*- coding: utf-8 -*-
from page.business_page.hot_map_page import HotMapPage
import time
from allure import MASTER_HELPER as allure


# 热力图页面操作
class HotMapHandle(object):
    def __init__(self,driver):
        self.hot_map_page = HotMapPage(driver)

    # 点击热力图返回按钮
    @allure.step("点击热力图返回按钮")
    def click_hotmap_back(self):
        self.hot_map_page.get_hotmap_back().click()
        return self

    # 判断订单按钮是否展示
    @allure.step("判断订单按钮是否展示")
    def judge_order_button(self):
        if self.hot_map_page.get_order_button().is_displayed():
            return True