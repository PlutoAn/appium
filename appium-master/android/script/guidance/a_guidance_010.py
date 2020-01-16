# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_010(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-010
    # Des: 检查新手引导年龄标签页UI
    def guidance_010(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击看看再说>>
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male')
        maleIcon.click()

        # 3.text“－选择你的年龄标签－”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的年龄标签-")')

        # 4.button"50后"，“60后”，“70后”，“80后”，“90后”，“00后”
        button50 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_50')
        self.assertIsNotNone(button50)

        button60 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_60')
        self.assertIsNotNone(button60)

        button70 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_70')
        self.assertIsNotNone(button70)

        button80 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_80')
        self.assertIsNotNone(button80)

        button90 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_90')
        self.assertIsNotNone(button90)

        button00 = self.driver.find_element_by_id('fm.qingting.qtradio:id/age_00')
        self.assertIsNotNone(button00)

if __name__ == '__main__':
    unittest.main()