# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from page.business_page.trip_page import TripPage
import time
from allure import MASTER_HELPER as allure


# 行程中页面操作
class TripPageHandle(object):
    def __init__(self, driver):
        self.trip_page = TripPage(driver)

    # 点击接单按钮
    def click_order_button(self):
        self.trip_page.get_order_button().click()
        return self

    # 获取页面title
    def get_trip_page_title(self, page_name):
        if page_name == "行程详情":
            title_text = self.trip_page.get_trip_info_title().text
        elif page_name == "确认账单":
            title_text = self.trip_page.get_bill_page_title().text
        elif page_name == "行程结束":
            title_text = self.trip_page.get_finish_order_page_title().text
        elif page_name == "等乘客":
            title_text = self.trip_page.get_wait_page_title().text
        else:
            title_text = self.trip_page.get_page_title().text
        return title_text

    # 点击行程详情入口
    def click_trip_into_btn(self):
        self.trip_page.get_trip_info().click()
        return self

    # 滑动按钮
    def slide_button(self):
        if self.trip_page.get_slider_btn().is_displayed():
            self.slide_button()
        return self

    # 点击返回按钮
    def click_back_btn(self, page_name):
        if page_name == "行程详情":
            self.trip_page.get_trip_info_back_btn().click()
        elif page_name == "确认账单":
            self.trip_page.get_bill_page_back_btn().click()
        return self

    # 点击休息按钮
    def click_rest_btn(self):
        self.trip_page.get_rest_btn().click()
        return self

    # 点击继续接单按钮
    def click_continue_btn(self):
        self.trip_page.get_continue_btn().click()

    # 快车实时单主流程
    def express_trip_main(self):
        # =========判断是否进入播单页面
        # WebDriverWait(self.driver,60).until(self.get_order_type().is_displayed())
        time.sleep(5)
        # 判断是否有接单按钮，有的话点击
        if self.trip_page.get_order_button().is_displayed():
            self.trip_page.get_order_button().click()
        # =========进入接乘客页面
        # WebDriverWait(self.driver,10).until(self.get_trip_page_title("接乘客") == "接乘客快车乘客")
        if self.get_trip_page_title("接乘客") == "接乘客快车乘客":
            # 点击行程详情入口
            self.click_trip_into_btn()
            # 点击行程详情页返回按钮
            self.click_back_btn("行程详情")
            print(self.trip_page.get_passenger_card_phone().text)
            print(self.trip_page.get_passenger_card_address_from().text)
            print(self.trip_page.get_passenger_card_address_to().text)
            if self.trip_page.get_slider_btn().text == "到达约定地点":
                self.slide_button()
        # ===========进入等乘客页面
        # WebDriverWait(self.driver, 10).until(self.get_trip_page_title("等乘客") == "等快车乘客")
        time.sleep(5)
        if self.get_trip_page_title("等乘客") == "等快车乘客":
            # 点击行程详情入口
            self.click_trip_into_btn()
            # 点击行程详情页返回按钮
            self.click_back_btn("行程详情")
            if self.trip_page.get_slider_btn().text == "接到乘客":
                self.slide_button()
        # ============进入送乘客页面
        time.sleep(5)
        # WebDriverWait(self.driver, 10).until(self.get_trip_page_title("送乘客") == "送快车乘客")
        if self.get_trip_page_title("送乘客") == "送快车乘客":
            # 点击行程详情入口
            self.click_trip_into_btn()
            # 点击行程详情页返回按钮
            self.click_back_btn("行程详情")
            print(self.trip_page.get_passenger_card_phone().text)
            print(self.trip_page.get_passenger_card_address_from().text)
            print(self.trip_page.get_passenger_card_address_to().text)
            if self.trip_page.get_slider_btn().text == "到达约定地点":
                self.slide_button()
        # ============进入确认账单页
        time.sleep(5)
        # WebDriverWait(self.driver, 10).until(self.get_trip_page_title("确认账单") == "确认账单")
        if self.get_trip_page_title("确认账单") == "确认账单":
            if self.trip_page.get_slider_btn().text == "发起收款":
                self.slide_button()
        # ============进入行程结束页
        time.sleep(5)
        # WebDriverWait(self.driver, 10).until(self.get_trip_page_title("行程结束") == "行程结束")
        if self.get_trip_page_title("行程结束") == "行程结束":
            print(self.trip_page.get_pay_status().text)
            print(self.trip_page.get_cost_value().text)
            self.click_continue_btn()

