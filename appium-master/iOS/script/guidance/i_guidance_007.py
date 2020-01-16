# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_007(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-007
    # Des: 检查新手引导性别页UI
    def guidance_007(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击看看再说>>
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()

        # 2.text“收听喜好小测试”
        loginType = self.driver.find_element_by_accessibility_id(u'收听喜好小测试')
        loginTypeText = loginType.get_attribute('name')
        self.assertEqual(loginTypeText, u'收听喜好小测试')

        # # 3.text“－选择你的性别－”
        # genderPageTitle = self.driver.find_element_by_accessibility_id(u'－选择你的性别－')
        # genderPageTitleText = genderPageTitle.get_attribute('name')
        # self.assertEqual(loginTypeText, u'－选择你的性别－')

        # 4.男icon
        maleIcon = self.driver.find_element_by_accessibility_id('gender_male_unselect')
        self.assertIsNotNone(maleIcon)

        # 5.text"男"
        male = self.driver.find_element_by_accessibility_id('男')
        maleText = male.get_attribute('name')
        self.assertEqual(maleText, u'男')

        # 6.女icon
        femaleIcon = self.driver.find_element_by_accessibility_id('gender_female_unselect')
        self.assertIsNotNone(femaleIcon)

        # 7.text"女"
        male = self.driver.find_element_by_accessibility_id('女')
        maleText = male.get_attribute('name')
        self.assertEqual(maleText, u'女')

if __name__ == '__main__':
    unittest.main()