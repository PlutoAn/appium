# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_008(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-008
    # Des: 性别选择页选择男性别后跳转至年龄标签页
    def guidance_008(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击看看再说>>
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_accessibility_id('gender_male_unselect')
        maleIcon.click()

        # # 3.text“－选择你的年龄标签－”
        # agePageTitle = self.driver.find_element_by_accessibility_id(u'－选择你的年龄标签－')
        # agePageTitleText = agePageTitle.get_attribute('name')
        # self.assertEqual(agePageTitleText, u'－选择你的年龄标签－')

if __name__ == '__main__':
    unittest.main()