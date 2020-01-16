# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_004(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-004
    # Des: 检查新手引导手机注册页跳转
    def guidance_004(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击手机icon
        phoneIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_phone')
        phoneIcon.click()

        # 2.title“手机注册”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("手机注册")')

if __name__ == '__main__':
    unittest.main()