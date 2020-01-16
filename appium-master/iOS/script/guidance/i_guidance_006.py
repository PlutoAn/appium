# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_006(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-006
    # Des: 检查手机注册页返回button
    def guidance_006(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击手机icon
        phoneIcon = self.driver.find_element_by_accessibility_id(u'手机登陆按钮')
        phoneIcon.click()

        # 2.title“注册新账号”
        registerTitle = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="注册新账号"]')
        registerTitleText = registerTitle.get_attribute('name')
        self.assertEqual(registerTitleText, u'注册新账号')

        # 3.点击“返回”button
        backbutton = self.driver.find_element_by_accessibility_id(u'返回')
        backbutton.click()

        loginType = self.driver.find_element_by_accessibility_id(u'-请选择登录方式-')
        loginTypeText = loginType.get_attribute('name')
        self.assertEqual(loginTypeText, u'-请选择登录方式-')

if __name__ == '__main__':
    unittest.main()