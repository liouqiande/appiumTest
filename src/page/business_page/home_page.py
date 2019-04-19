# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/home_page_element.yaml"

    # 定位个人中心入口
    def get_person_center(self):
        logging.info("个人中心入口")
        person_center = self.locate_element(self.file_path, "person_center")
        return person_center

    # 定位首页tab
    def get_homepage_tab(self):
        logging.info("定位首页tab")
        homepage_tab = self.locate_element(self.file_path, "homepage_tab")
        return homepage_tab

    # 定位小桔车服tab
    def get_carlife_tab(self):
        logging.info("定位小桔车服tab")
        carlife_tab = self.locate_element(self.file_path, "carlife_tab")
        return carlife_tab

    # 定位消息中心入口
    def get_msg_center(self):
        logging.info("定位消息中心入口")
        msg_center = self.locate_element(self.file_path, "msg_center")
        return msg_center

    # 定位服务分
    def get_service_count(self):
        logging.info("定位服务分")
        service_count = self.locate_element(self.file_path, "service_count")
        return service_count

    # 定位今日流水
    def get_today_money(self):
        logging.info("定位今日流水")
        today_money = self.locate_element(self.file_path, "today_money")
        return today_money

    # 定位今日接单
    def get_today_order(self):
        logging.info("定位今日接单")
        today_order = self.locate_element(self.file_path, "today_order")
        return today_order

    # 定位在线时长
    def get_today_service_time(self):
        logging.info("定位在线时长")
        today_service_time = self.locate_element(self.file_path, "today_service_time")
        return today_service_time

    # 定位数据看板入口
    def get_data_more_view(self):
        logging.info("定位数据看板入口")
        data_more_view = self.locate_element(self.file_path, "data_more_view")
        return data_more_view

    # 定位合规按钮
    def get_compliance(self):
        logging.info("定位合规按钮")
        compliance = self.locate_element(self.file_path, "compliance")
        return compliance

    # 定位奖励按钮
    def get_reward(self):
        logging.info("定位奖励按钮")
        reward = self.locate_element(self.file_path, "reward")
        return reward

    # 定位热力图按钮
    def get_hot_map(self):
        logging.info("定位热力图按钮")
        hot_map = self.locate_element(self.file_path, "hot_map")
        return hot_map

    # 定位更多按钮
    def get_more_btn(self):
        logging.info("定位更多按钮")
        more_btn = self.locate_element(self.file_path, "more_btn")
        return more_btn

    # 定位消息盒子入口
    def get_msg_center_content(self):
        logging.info("定位消息盒子入口")
        msg_center_content = self.locate_element(self.file_path, "msg_center_content")
        return msg_center_content

    # 定位安全球
    def get_safety_guard_shield(self):
        logging.info("定位安全球")
        safety_guard_shield = self.locate_element(self.file_path, "safety_guard_shield")
        return safety_guard_shield

    # 定位模式设置入口
    def get_set_mode_btn(self):
        logging.info("定位模式设置入口")
        set_mode_btn = self.locate_element(self.file_path, "set_mode_btn")
        return set_mode_btn

    # 定位接单/休息按钮
    def get_start_off_btn(self):
        logging.info("定位接单/休息按钮")
        start_off_btn = self.locate_element(self.file_path, "start_off_btn")
        return start_off_btn

    # 定位听单状态
    def get_listening_status(self):
        logging.info("定位听单状态")
        listening_status = self.locate_element(self.file_path, "listening_status")
        return listening_status