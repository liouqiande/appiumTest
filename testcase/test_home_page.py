# -*- coding: utf-8 -*-
from allure import MASTER_HELPER as allure
from common.init_driver import init_driver
from handle.login_handle import LoginHandle
from handle.home_page_handle import HomePageHandle
from handle.person_center_page_handle import PersonCenterHandle
from handle.h5_page_handle import H5PageHandle
from handle.msg_center_page_handle import MsgCenterHandle
from handle.hot_map_page_handle import HotMapHandle
from handle.mode_setting_page_handle import ModeSettingHandle
import time


@allure.feature("首页")
class TestHomePage(object):
    @classmethod
    def setup_class(cls):
        cls.driver = init_driver()
        login_handle = LoginHandle(cls.driver)
        login_handle.login_main("xxxx", "xxxx")
        cls.home_page_handle = HomePageHandle(cls.driver)
        cls.person_center_handle = PersonCenterHandle(cls.driver)
        cls.h5_page_handle = H5PageHandle(cls.driver)
        cls.msg_center_handle = MsgCenterHandle(cls.driver)
        cls.hot_map_handle = HotMapHandle(cls.driver)
        cls.mode_setting_handle = ModeSettingHandle(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    @allure.story("进入首页")
    def test_click_homepage_tab(self):

        assert TestHomePage.home_page_handle.get_mode_setting_btn_text() == "模式"

    @allure.story("点击个人中心入口")
    def test_click_person_center(self):
        TestHomePage.home_page_handle.click_person_center()
        assert TestHomePage.person_center_handle.get_person_center_text() == "点击进入个人主页"
        TestHomePage.person_center_handle.click_person_center_back()

    @allure.story("点击小桔车服tab")
    def test_click_carlife_tab(self):
        TestHomePage.home_page_handle.click_carlife_tab()
        assert TestHomePage.h5_page_handle.judge_car_life_buttom_btn() == True
        TestHomePage.home_page_handle.click_homepage_tab()

    @allure.story("点击消息中心入口")
    def test_click_msg_center(self):
        TestHomePage.home_page_handle.click_msg_center()
        assert TestHomePage.msg_center_handle.get_msg_center_text() == "消息"
        TestHomePage.msg_center_handle.click_msg_center_back()

    @allure.story("点击服务分")
    def test_click_service_count(self):
        TestHomePage.home_page_handle.click_service_count()
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "服务分"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击今日流水")
    def test_click_today_money(self):
        TestHomePage.home_page_handle.click_today_money()
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "我的流水"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击今日接单")
    def test_click_today_order(self):
        TestHomePage.home_page_handle.click_today_order()
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "我的行程"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击合规按钮")
    def test_click_compliance(self):
        TestHomePage.home_page_handle.click_compliance()
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "合规认证"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击奖励按钮")
    def test_click_reward(self):
        TestHomePage.home_page_handle.click_reward()
        time.sleep(2)
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "奖励活动"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击热力图按钮")
    def test_click_hot_map(self):
        TestHomePage.home_page_handle.click_hot_map()
        assert TestHomePage.hot_map_handle.judge_order_button() == True
        TestHomePage.hot_map_handle.click_hotmap_back()

    @allure.story("点击更多按钮")
    def test_click_more_btn(self):
        TestHomePage.home_page_handle.click_more_btn()
        assert TestHomePage.h5_page_handle.get_h5_page_title_text() == "全部功能"
        TestHomePage.h5_page_handle.click_h5_page_back_btn()

    @allure.story("点击消息盒子入口")
    def test_click_msg_center_content(self):
        TestHomePage.home_page_handle.click_msg_center_content()
        assert TestHomePage.msg_center_handle.get_msg_center_text() == "消息"
        TestHomePage.msg_center_handle.click_msg_center_back()

    # @allure.story("点击安全球")
    # def test_click_safety_guard_shield(self):
    #     home_page = setup_function()
    #     home_page[0].click_safety_guard_shield()
    #     time.sleep(3)
    #     print(home_page[1].page_source)
    #
    @allure.story("点击模式按钮")
    def test_click_set_mode_btn(self):
        TestHomePage.home_page_handle.click_set_mode_btn()
        assert TestHomePage.mode_setting_handle.get_mode_setting_title_text() == "模式设置"
        TestHomePage.mode_setting_handle.click_mode_setting_back()

    @allure.story("点击接单按钮")
    def test_click_start_off_btn(self):
        TestHomePage.home_page_handle.click_start_off_btn()
        assert TestHomePage.home_page_handle.get_listening_status_text() == "听单中"