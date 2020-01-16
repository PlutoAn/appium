# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_007(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-007
    # Des: 检查新手引导性别页UI
    def guidance_007(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击看看再说>>
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()

        # 2.text“收听喜好小测试”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("收听喜好小测试")')

        # 3.text“－选择你的性别－”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的性别-")')

        # 4.男icon
        maleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male')
        self.assertIsNotNone(maleIcon)

        # 5.text"男"
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("男")')

        # 6.女icon
        femaleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_female')
        self.assertIsNotNone(femaleIcon)

        # 7.text"女"
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("女")')

if __name__ == '__main__':
    unittest.main()