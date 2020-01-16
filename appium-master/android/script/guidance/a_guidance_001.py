# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import installApp

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class a_guidance_001(unittest.TestCase):
    def setUp(self):
        os.popen("adb uninstall 'fm.qingting.qtradio'")
        installApp.install()
        time.sleep(3)

        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-001
    # Des: 新装app打开时，允许获取定位权限请求。
    def guidance_001(self):

        time.sleep(2)
        # 切换到alert窗口(Access location)
        alert = self.driver.switch_to_alert()
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

if __name__ == '__main__':
    unittest.main()