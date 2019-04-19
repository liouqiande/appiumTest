# -*- coding: utf-8 -*-
import pytest
from allure import MASTER_HELPER as allure
from common.init_driver import init_driver
from handle.login_handle import LoginHandle
from handle.home_page_handle import HomePageHandle
from handle.trip_page_handle import TripPageHandle

@pytest.fixture(scope="class")


@allure.feature("首页")
class TestExpressTrip(object):

    @classmethod
    def setup_class(cls):
        cls.driver = init_driver()
        login_handle = LoginHandle(cls.driver)
        login_handle.login_main("xxxx", "xxxx")
        cls.home_page_handle = HomePageHandle(cls.driver)
        cls.trip_page_handle = TripPageHandle(cls.driver)

    def test_express_trip_main(self):
        TestExpressTrip.home_page_handle.click_start_off_btn()
