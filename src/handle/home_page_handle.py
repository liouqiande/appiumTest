# -*- coding: utf-8 -*-
from page.business_page.home_page import HomePage
import time
from allure import MASTER_HELPER as allure

# 首页操作
class HomePageHandle(object):
    def __init__(self,driver):
        self.home_page = HomePage(driver)

    # 点击个人中心按钮
    @allure.step("点击个人中心按钮")
    def click_person_center(self):
        self.home_page.get_person_center().click()
        self.home_page.getScreenShot("个人中心")
        return self

    # 点击首页tab
    @allure.step("点击首页tab")
    def click_homepage_tab(self):
        self.home_page.get_homepage_tab().click()
        self.home_page.getScreenShot("首页")
        return self

    # 点击小桔车服tab
    @allure.step("点击小桔车服tab")
    def click_carlife_tab(self):
        self.home_page.get_carlife_tab().click()
        self.home_page.getScreenShot("小桔车服")
        return self

    # 点击消息中心入口
    @allure.step("点击消息中心入口")
    def click_msg_center(self):
        self.home_page.get_msg_center().click()
        self.home_page.getScreenShot("消息中心")
        return self

    # 点击服务分
    @allure.step("点击服务分")
    def click_service_count(self):
        self.home_page.get_service_count().click()
        self.home_page.getScreenShot("服务分")
        return self

    # 点击今日流水
    @allure.step("点击今日流水")
    def click_today_money(self):
        self.home_page.get_today_money().click()
        self.home_page.getScreenShot("今日流水")
        return self

    # 点击今日接单
    @allure.step("点击今日接单")
    def click_today_order(self):
        self.home_page.get_today_order().click()
        self.home_page.getScreenShot("今日接单")
        return self

    # 点击在线时长
    @allure.step("点击在线时长")
    def click_today_service_time(self):
        self.home_page.get_today_service_time().click()
        self.home_page.getScreenShot("在线时长")
        return self

    # 点击数据看板入口
    @allure.step("点击数据看板入口")
    def click_data_more_view(self):
        self.home_page.get_data_more_view().click()
        self.home_page.getScreenShot("数据看板")
        return self

    # 点击合规按钮
    @allure.step("点击合规按钮")
    def click_compliance(self):
        self.home_page.get_compliance().click()
        self.home_page.getScreenShot("合规")
        return self

    # 点击奖励按钮
    @allure.step("点击奖励按钮")
    def click_reward(self):
        self.home_page.get_reward().click()
        self.home_page.getScreenShot("奖励")
        return self

    # 点击热力图按钮
    @allure.step("点击热力图按钮")
    def click_hot_map(self):
        self.home_page.get_hot_map().click()
        self.home_page.getScreenShot("热力图")
        return self

    # 点击更多按钮
    @allure.step("点击更多按钮")
    def click_more_btn(self):
        self.home_page.get_more_btn().click()
        self.home_page.getScreenShot("全部功能")
        return self

    # 点击消息盒子入口
    @allure.step("点击消息盒子入口")
    def click_msg_center_content(self):
        self.home_page.get_msg_center_content().click()
        self.home_page.getScreenShot("消息")
        return self

    # 点击安全球
    @allure.step("点击安全球")
    def click_safety_guard_shield(self):
        self.home_page.get_safety_guard_shield().click()
        self.home_page.getScreenShot("安全中心")
        return self

    # 点击模式按钮
    @allure.step("点击模式按钮")
    def click_set_mode_btn(self):
        self.home_page.get_set_mode_btn().click()
        self.home_page.getScreenShot("模式设置")
        return self

    # 点击接单按钮
    @allure.step("点击接单按钮")
    def click_start_off_btn(self):
        self.home_page.get_start_off_btn().click()
        self.home_page.getScreenShot("接单中")
        return self

    # 获取模式设置按钮文案
    @allure.step("获取模式设置按钮文案")
    def get_mode_setting_btn_text(self):
        text = self.home_page.get_set_mode_btn().get_attribute("text")
        return text

    # 获取听单状态文案
    @allure.step("获取听单状态文案")
    def get_listening_status_text(self):
        text = self.home_page.get_listening_status().get_attribute("text")
        return text