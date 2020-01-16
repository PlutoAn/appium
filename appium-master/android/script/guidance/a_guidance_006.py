# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_006(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-006
    # Des: 检查手机注册页返回button
    def guidance_006(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击手机icon
        phoneIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_phone')
        phoneIcon.click()

        # 2.title“手机注册”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("手机注册")')

        # 3.点击“返回”button
        backbutton = self.driver.find_element_by_id('fm.qingting.qtradio:id/welcome_back_btn')
        backbutton.click()

        loginType = self.driver.find_element_by_android_uiautomator('new UiSelector().text("-请选择注册/登录方式-")')
        self.assertIsNotNone(loginType)

if __name__ == '__main__':
    unittest.main()