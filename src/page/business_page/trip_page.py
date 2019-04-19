# -*- coding: utf-8 -*-
from page.base_page import BasePage
import logging


class TripPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_path = "D:/pyproject/DidiDriverTestProject/config/trip_element.yaml"

    # 定位播单页订单类型
    def get_order_type(self):
        logging.info("定位播单页订单类型")
        order_type = self.locate_element(self.file_path, "order_type")
        return order_type

    # 定位接单按钮
    def get_order_button(self):
        logging.info("定位接单按钮")
        order_button = self.locate_element(self.file_path, "order_button")
        return order_button

    # 定位接乘客、送乘客页面title
    def get_page_title(self):
        logging.info("定位接乘客、送乘客页面title")
        pick_up_page_title = self.locate_element(self.file_path, "page_title")
        return pick_up_page_title

    # 定位接乘客、送乘客页面title
    def get_wait_page_title(self):
        logging.info("定位接乘客、送乘客页面title")
        wait_page_title = self.locate_element(self.file_path, "wait_page_title")
        return wait_page_title

    # 定位行程详情入口
    def get_trip_info(self):
        logging.info("定位行程详情入口")
        trip_info = self.locate_element(self.file_path, "trip_info")
        return trip_info

    # 定位目的地信息
    def get_destination_info(self):
        logging.info("定位目的地信息")
        destination_info = self.locate_element(self.file_path, "destination_info")
        return destination_info

    # 定位eta信息
    def get_destination_eta_info(self):
        logging.info("定位eta信息")
        destination_eta_info = self.locate_element(self.file_path, "destination_eta_info")
        return destination_eta_info

    # 定位导航按钮
    def get_nav_btn(self):
        logging.info("定位导航按钮")
        nav_btn = self.locate_element(self.file_path, "nav_btn")
        return nav_btn

    # 定位消息栏文案
    def get_msg_box(self):
        logging.info("定位消息栏文案")
        msg_box = self.locate_element(self.file_path, "msg_box")
        return msg_box

    # 定位乘客信息卡片-乘客手机尾号
    def get_passenger_card_phone(self):
        logging.info("定位乘客信息卡片-乘客手机尾号")
        passenger_card_phone = self.locate_element(self.file_path, "passenger_card_phone")
        return passenger_card_phone

    # 定位乘客信息卡片-乘客起点信息
    def get_passenger_card_address_from(self):
        logging.info("定位乘客信息卡片-乘客起点信息")
        passenger_card_address_from = self.locate_element(self.file_path, "passenger_card_address_from")
        return passenger_card_address_from

    # 定位乘客信息卡片-乘客终点信息
    def get_passenger_card_address_to(self):
        logging.info("定位乘客信息卡片-乘客终点信息")
        passenger_card_address_to = self.locate_element(self.file_path, "passenger_card_address_to")
        return passenger_card_address_to

    # 定位乘客信息卡片-im按钮
    def get_passenger_card_im_btn(self):
        logging.info("定位乘客信息卡片-im按钮")
        passenger_card_im_btn = self.locate_element(self.file_path, "passenger_card_im_btn")
        return passenger_card_im_btn

    # 定位乘客信息卡片-phone按钮
    def get_passenger_card_phone_btn(self):
        logging.info("定位乘客信息卡片-phone按钮")
        passenger_card_phone_btn = self.locate_element(self.file_path, "passenger_card_phone_btn")
        return passenger_card_phone_btn

    # 定位全屏导航页导航距离
    def get_map_router_distance(self):
        logging.info("定位全屏导航页导航距离")
        map_router_distance = self.locate_element(self.file_path, "map_router_distance")
        return map_router_distance

    # 定位全屏导航页关闭按钮
    def get_nav_close(self):
        logging.info("定位全屏导航页关闭按钮")
        nav_close = self.locate_element(self.file_path, "nav_close")
        return nav_close

    # 定位滑动按钮
    def get_slider_btn(self):
        logging.info("定位滑动按钮")
        slider_btn = self.locate_element(self.file_path, "slider_btn")
        return slider_btn

    # 定位行程详情页title
    def get_trip_info_title(self):
        logging.info("定位行程详情页title")
        trip_info_title = self.locate_element(self.file_path, "trip_info_title")
        return trip_info_title

    # 定位行程详情页返回按钮
    def get_trip_info_back_btn(self):
        logging.info("定位行程详情页返回按钮")
        trip_info_back_btn = self.locate_element(self.file_path, "trip_info_back_btn")
        return trip_info_back_btn

    # 定位乘客手机尾号
    def get_trip_info_passenger_phone(self):
        logging.info("定位乘客手机尾号")
        trip_info_passenger_phone = self.locate_element(self.file_path, "trip_info_passenger_phone")
        return trip_info_passenger_phone

    # 定位乘客起点信息
    def get_trip_info_address_from(self):
        logging.info("定位乘客起点信息")
        trip_info_address_from = self.locate_element(self.file_path, "trip_info_address_from")
        return trip_info_address_from

    # 定位乘客终点信息
    def get_trip_info_address_to(self):
        logging.info("定位乘客终点信息")
        trip_info_address_to = self.locate_element(self.file_path, "trip_info_address_to")
        return trip_info_address_to

    # 定位行程详情页im按钮
    def get_trip_info_im_btn(self):
        logging.info("定位乘客终点信息")
        trip_info_im_btn = self.locate_element(self.file_path, "trip_info_im_btn")
        return trip_info_im_btn

    # 定位行程详情页phone按钮
    def get_trip_info_phone_btn(self):
        logging.info("定位乘客终点信息")
        trip_info_phone_btn = self.locate_element(self.file_path, "trip_info_phone_btn")
        return trip_info_phone_btn

    # 定位取消订单按钮
    def get_cancle_order(self):
        logging.info("定位取消订单按钮")
        cancle_order = self.locate_element(self.file_path, "cancle_order")
        return cancle_order

    # 定位联系不上乘客按钮
    def get_can_not_contact_passenger(self):
        logging.info("定位联系不上乘客按钮")
        can_not_contact_passenger = self.locate_element(self.file_path, "can_not_contact_passenger")
        return can_not_contact_passenger

    # 定位修改目的地按钮
    def get_change_address_to(self):
        logging.info("定位修改目的地按钮")
        change_address_to = self.locate_element(self.file_path, "change_address_to")
        return change_address_to

    # 定位关闭行程中派单按钮
    def get_close_order_in_trip(self):
        logging.info("定位关闭行程中派单按钮")
        close_order_in_trip = self.locate_element(self.file_path, "close_order_in_trip")
        return close_order_in_trip

    # 定位待出发订单
    def get_pending_order(self):
        logging.info("定位待出发订单")
        pending_order = self.locate_element(self.file_path, "pending_order")
        return pending_order

    # 定位客服
    def get_customer_service(self):
        logging.info("定位客服")
        customer_service = self.locate_element(self.file_path, "customer_service")
        return customer_service

    # 定位一键报警
    def get_key_alarm(self):
        logging.info("定位一键报警")
        key_alarm = self.locate_element(self.file_path, "key_alarm")
        return key_alarm

    # 定位更换手机号
    def get_change_phone(self):
        logging.info("定位更换手机号")
        change_phone = self.locate_element(self.file_path, "change_phone")
        return change_phone

    # 定位账单页title
    def get_bill_page_title(self):
        logging.info("定位账单页title")
        bill_page_title = self.locate_element(self.file_path, "bill_page_title")
        return bill_page_title

    # 定位账单页返回按钮
    def get_bill_page_back_btn(self):
        logging.info("定位账单页返回按钮")
        bill_page_back_btn = self.locate_element(self.file_path, "bill_page_back_btn")
        return bill_page_back_btn

    # 定位账单金额
    def get_bill_fee_amount(self):
        logging.info("定位账单金额")
        bill_fee_amount = self.locate_element(self.file_path, "bill_fee_amount")
        return bill_fee_amount

    # 定位附加费title
    def get_bill_extra_fee_title(self):
        logging.info("定位附加费title")
        bill_extra_fee_title = self.locate_element(self.file_path, "bill_extra_fee_title")
        return bill_extra_fee_title

    # 定位高速费
    def get_highway_fee(self):
        logging.info("定位高速费")
        highway_fee = self.locate_element(self.file_path, "highway_fee")
        return highway_fee

    # 定位路桥费
    def get_toll_fee(self):
        logging.info("定位路桥费")
        toll_fee = self.locate_element(self.file_path, "toll_fee")
        return toll_fee

    # 定位停车费
    def get_parking_fee(self):
        logging.info("定位停车费")
        parking_fee = self.locate_element(self.file_path, "parking_fee")
        return parking_fee

    # 定位洗车费
    def get_car_washing_fee(self):
        logging.info("定位洗车费")
        car_washing_fee = self.locate_element(self.file_path, "car_washing_fee")
        return car_washing_fee

    # 定位行程结束页title
    def get_finish_order_page_title(self):
        logging.info("定位行程结束页title")
        finish_order_page_title = self.locate_element(self.file_path, "finish_order_page_title")
        return finish_order_page_title

    # 定位行程结束页更多按钮
    def get_finish_order_page_more_btn(self):
        logging.info("定位行程结束页更多按钮")
        more_btn = self.locate_element(self.file_path, "more_btn")
        return more_btn

    # 定位支付状态
    def get_pay_status(self):
        logging.info("定位支付状态")
        pay_status = self.locate_element(self.file_path, "pay_status")
        return pay_status

    # 定位支付金额
    def get_cost_value(self):
        logging.info("定位支付状态")
        cost_value = self.locate_element(self.file_path, "cost_value")
        return cost_value

    # 定位提问式评价title
    def get_tips(self):
        logging.info("定位提问式评价title")
        tips = self.locate_element(self.file_path, "tips")
        return tips

    # 定位提问式评价左按钮
    def get_left_btn(self):
        logging.info("定位提问式评价左按钮")
        left_btn = self.locate_element(self.file_path, "left_btn")
        return left_btn

    # 定位提问式评价右按钮
    def get_right_btn(self):
        logging.info("定位提问式评价左按钮")
        right_btn = self.locate_element(self.file_path, "right_btn")
        return right_btn

    # 定位五星评价title
    def get_star_view_title(self):
        logging.info("定位五星评价title")
        star_view_title = self.locate_element(self.file_path, "star_view_title")
        return star_view_title

    # 定位五星评价区域
    def get_star_view(self):
        logging.info("定位五星评价区域")
        star_view = self.locate_element(self.file_path, "star_view")
        return star_view

    # 定位休息按钮
    def get_rest_btn(self):
        logging.info("定位休息按钮")
        rest_btn = self.locate_element(self.file_path, "rest_btn")
        return rest_btn

    # 定位继续接单按钮
    def get_continue_btn(self):
        logging.info("定位休息按钮")
        continue_btn = self.locate_element(self.file_path, "continue_btn")
        return continue_btn