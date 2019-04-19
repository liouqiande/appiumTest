# -*- coding: utf-8 -*-
from page.business_page.h5_page import H5Page
import time
from allure import MASTER_HELPER as allure

# h5页面操作
class H5PageHandle(object):
    def __init__(self,driver):
        self.h5_page = H5Page(driver)

    # 点击h5页面返回按钮
    @allure.step("点击h5页面返回按钮")
    def click_h5_page_back_btn(self):
        self.h5_page.get_h5_back_btn().click()
        return self

    # 判断小桔车服页面行车服务按钮已经展示
    @allure.step("判断小桔车服页面行车服务按钮已经展示")
    def judge_car_life_buttom_btn(self):
        if self.h5_page.get_car_life_buttom_btn().is_displayed():
            return True

    # 获取h5页面title文案
    @allure.step("获取h5页面title文案")
    def get_h5_page_title_text(self):
        text = self.h5_page.get_h5_page_title().get_attribute("text")
        return text