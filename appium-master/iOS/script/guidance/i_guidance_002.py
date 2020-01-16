# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_002(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-002
    # Des: 新装app打开时，允许通知权限请求。
    def guidance_002(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 检查新手引导首页UI
        # 1.登录体验logo
        logo = self.driver.find_element_by_accessibility_id('StartShowUpImage')
        self.assertIsNotNone(logo)

        # 2.text“-请选择登录方式-”
        loginType = self.driver.find_element_by_accessibility_id(u'-请选择登录方式-')
        loginTypeText = loginType.get_attribute('name')
        self.assertEqual(loginTypeText, u'-请选择登录方式-')

        # 3.手机，微信，新浪微博，qq，更多账号icon和text
        phoneIcon = self.driver.find_element_by_accessibility_id(u'手机登陆按钮')
        self.assertIsNotNone(phoneIcon)
        phoneText = self.driver.find_element_by_accessibility_id(u'手机')
        self.assertIsNotNone(phoneText)

        wechatIcon = self.driver.find_element_by_accessibility_id(u'微信登陆按钮')
        self.assertIsNotNone(wechatIcon)
        wechatText = self.driver.find_element_by_accessibility_id(u'微信')
        self.assertIsNotNone(wechatText)

        xinlangIcon = self.driver.find_element_by_accessibility_id(u'新浪微博登陆按钮')
        self.assertIsNotNone(xinlangIcon)
        xinlangText = self.driver.find_element_by_accessibility_id(u'新浪微博')
        self.assertIsNotNone(xinlangText)

        qqIcon = self.driver.find_element_by_accessibility_id(u'QQ登陆按钮')
        self.assertIsNotNone(qqIcon)
        qqText = self.driver.find_element_by_accessibility_id(u'QQ')
        self.assertIsNotNone(qqText)        

        moreLoginIcon = self.driver.find_element_by_accessibility_id(u'更多账户登陆按钮')
        self.assertIsNotNone(moreLoginIcon)
        moreLoginText = self.driver.find_element_by_accessibility_id(u'更多账户')
        self.assertIsNotNone(moreLoginText)

        # 4.看看再说>>
        helloButton = self.driver.find_element_by_accessibility_id(u'看看再说按钮')
        self.assertIsNotNone(helloButton)


if __name__ == '__main__':
    unittest.main()