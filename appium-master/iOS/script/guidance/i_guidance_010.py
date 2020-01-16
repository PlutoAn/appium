# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_010(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-010
    # Des: 检查新手引导年龄标签页UI
    def guidance_010(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击看看再说>>
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_accessibility_id('gender_male_unselect')
        maleIcon.click()

        # 等待年龄标签页面加载
        time.sleep(2)

        # # 3.text“－选择你的年龄标签－”
        # agePageTitle = self.driver.find_element_by_accessibility_id(u'－选择你的年龄标签－')
        # agePageTitleText = agePageTitle.get_attribute('name')
        # self.assertEqual(agePageTitleText, u'－选择你的年龄标签－')

        # 4.button"50后"，“60后”，“70后”，“80后”，“90后”，“00后”
        button50 = self.driver.find_element_by_accessibility_id('50后')
        self.assertIsNotNone(button50)

        button60 = self.driver.find_element_by_accessibility_id('60后')
        self.assertIsNotNone(button60)

        button70 = self.driver.find_element_by_accessibility_id('70后')
        self.assertIsNotNone(button70)

        button80 = self.driver.find_element_by_accessibility_id('80后')
        self.assertIsNotNone(button80)

        button90 = self.driver.find_element_by_accessibility_id('90后')
        self.assertIsNotNone(button90)

        button00 = self.driver.find_element_by_accessibility_id('00后')
        self.assertIsNotNone(button00)

if __name__ == '__main__':
    unittest.main()