# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_001(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        configParam.setReleaseParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-001
    # Des: 新装app打开时，允许通知权限请求。
    def guidance_001(self):

        # Wait alert
        time.sleep(3)

        # 切换到alert窗口(Access location)
        self.driver.switch_to_alert()
        ele = common.wait_for(self.driver, u'允许“蜻蜓FM”在您使用该应用时访问您的位置吗？', 3)
        if ele != 'False':
            # alert = self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="允许“蜻蜓FM”在您使用该应用时访问您的位置吗？"]')
            allowButton = self.driver.find_element_by_accessibility_id('允许')
            allowButton.click()

        time.sleep(2)
        # 切换到alert窗口(Send notifiCations)
        self.driver.switch_to_alert()
        # alert = self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="“蜻蜓FM”想给您发送通知"]')
        allowButton = self.driver.find_element_by_accessibility_id('允许')
        allowButton.click()

if __name__ == '__main__':
    unittest.main()