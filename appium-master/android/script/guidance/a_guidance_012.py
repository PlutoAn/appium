# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_012(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()
        self.driver.reset()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-012
    # Des: 选择年龄标签后的跳转
    def guidance_012(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击看看再说>>
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male')
        maleIcon.click()

        # 3.text“－选择你的年龄标签－”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的年龄标签-")')
        self.driver.find_element_by_id('fm.qingting.qtradio:id/age_90').click()

        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 15)
        self.driver.find_element_by_accessibility_id('分类') 

        time.sleep(2) 
        self.driver.tap([(540,1565),(0,0)])     

if __name__ == '__main__':
    unittest.main()