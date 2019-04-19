# -*- coding: utf-8 -*-
import yaml
from appium import webdriver


def init_driver():
    with open('D:/pyproject/DidiDriverTestProject/config/didi_driver_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['autoGrantPermissions'] = data['autoGrantPermissions']
    desired_caps['automationName'] = data['automationName']
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(15)
    return driver