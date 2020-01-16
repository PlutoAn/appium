# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_003(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-003
    # Des: 点击新手引导登录注册页“看看再说>>”
    def guidance_003(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击看看再说>>
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()

        # 2.text“收听喜好小测试”
        loginType = self.driver.find_element_by_accessibility_id(u'收听喜好小测试')
        loginTypeText = loginType.get_attribute('name')
        self.assertEqual(loginTypeText, u'收听喜好小测试')

if __name__ == '__main__':
    unittest.main()