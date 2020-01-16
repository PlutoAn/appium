# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_005(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-005
    # Des: 检查新手引导手机注册页UI
    def guidance_005(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击手机icon
        phoneIcon = self.driver.find_element_by_accessibility_id(u'手机登陆按钮')
        phoneIcon.click()

        # 2.title“注册新账号”
        registerTitle = self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="注册新账号"]')
        registerTitleText = registerTitle.get_attribute('name')
        self.assertEqual(registerTitleText, u'注册新账号')

        # 3.手机号输入placeholder
        phoneNumberTextFiled = self.driver.find_element_by_xpath('//XCUIElementTypeOther/XCUIElementTypeTextField')
        phoneNumberTextFileText = phoneNumberTextFiled.get_attribute('value')
        self.assertEqual(phoneNumberTextFileText, u'输入手机号码，仅限中国大陆手机号码')

        # 4.密码输入placeholder
        pwdTextFiled = self.driver.find_element_by_xpath('//XCUIElementTypeOther/XCUIElementTypeSecureTextField')
        pwdTextFileText = pwdTextFiled.get_attribute('value')
        self.assertEqual(pwdTextFileText, u'设置登录密码 不少于6位')

        # 5.“注册”button
        registerButton = self.driver.find_element_by_accessibility_id('注册')
        registerButtonText = registerButton.get_attribute('name')
        self.assertEqual(registerButtonText, u'注册')

        # 5.其他注册方式
        otherRegisterType = self.driver.find_element_by_accessibility_id('—其它注册方式—')
        otherRegisterTypeText = otherRegisterType.get_attribute('name')
        self.assertEqual(otherRegisterTypeText, u'—其它注册方式—')

if __name__ == '__main__':
    unittest.main()