# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_011(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-011
    # Des: 选择年龄标签后的跳转
    def guidance_011(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击看看再说>>
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male')
        maleIcon.click()

        # 3.text“－选择你的年龄标签－”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的年龄标签-")')

        # 4.选择年龄标签后的跳转
        ageArray = ['age_50','age_60','age_70','age_80','age_90','age_00']
        for age in range(len(ageArray)):
            ageId = "fm.qingting.qtradio:id/" + ageArray[age]

            # select age
            self.driver.find_element_by_id(ageId).click()
            common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 5)
            self.driver.find_element_by_accessibility_id('分类')

            self.driver.reset()

            common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 10)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()
            self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male').click()

if __name__ == '__main__':
    unittest.main()