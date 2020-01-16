# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_009(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-009
    # Des: 性别选择页选择女性别后跳转至年龄标签页
    def guidance_009(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击看看再说>>
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()

        # 2.点击“男”icon
        femaleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_female')
        femaleIcon.click()

        # 3.text“－选择你的年龄标签－”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的年龄标签-")')

if __name__ == '__main__':
    unittest.main()