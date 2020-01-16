# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_005(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-005
    # Des: 检查新手引导手机注册页UI
    def guidance_005(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 1.点击手机icon
        phoneIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_phone')
        phoneIcon.click()

        # 2.title“手机注册”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("手机注册")')

        # 3.手机号输入placeholder
        phoneNumberTextFiled = self.driver.find_element_by_id('fm.qingting.qtradio:id/phone_number_et')
        phoneNumberTextFileText = phoneNumberTextFiled.get_attribute('name')
        self.assertEqual(phoneNumberTextFileText, u'输入手机号码，仅限中国大陆手机号码')

        # 4.密码输入placeholder
        pwdTextFiled = self.driver.find_element_by_id('fm.qingting.qtradio:id/passwd_et')
        pwdTextFileText = pwdTextFiled.get_attribute('name')
        self.assertEqual(pwdTextFileText, u'设置登录密码，不少于6位')

        # 5.“注册”button
        registerButton = self.driver.find_element_by_id('fm.qingting.qtradio:id/signup_btn')
        registerButtonText = registerButton.get_attribute('name')
        self.assertEqual(registerButtonText, u'注册')

        # 6.已有账号？点此登录
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("已有账号？")')
        login = self.driver.find_element_by_android_uiautomator('new UiSelector().text("点此登录")')
        self.assertTrue(login.get_attribute('clickable'))

        # 7.Terms
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击注册按钮或其他注册方式代表你已阅读并同意")')
        terms = self.driver.find_element_by_android_uiautomator('new UiSelector().text("蜻蜓FM软件许可及服务协议")')
        self.assertTrue(terms.get_attribute('clickable'))

if __name__ == '__main__':
    unittest.main()