# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_guidance_002(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-002
    # Des: 检查新手引导登录页UI。
    def guidance_002(self):

        # Wait新手引导首页
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 3)

        # 检查新手引导首页UI
        # 1.登录体验logo
        logo = self.driver.find_element_by_accessibility_id('登录提示')
        self.assertIsNotNone(logo)

        # 2.text“-请选择注册/登录方式-”
        loginType = self.driver.find_element_by_android_uiautomator('new UiSelector().text("-请选择注册/登录方式-")')

        # 3.手机，微信，新浪微博，qq，更多账号icon和text
        phoneIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_phone')
        self.assertIsNotNone(phoneIcon)

        wechatIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_wx')
        self.assertIsNotNone(wechatIcon)

        xinlangIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_wb')
        self.assertIsNotNone(xinlangIcon)

        qqIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_qq')
        self.assertIsNotNone(qqIcon)      

        moreLoginIcon = self.driver.find_element_by_id('fm.qingting.qtradio:id/btn_more')
        self.assertIsNotNone(moreLoginIcon)

        # 4.看看再说>>
        helloButton = self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")')
        self.assertIsNotNone(helloButton)


if __name__ == '__main__':
    unittest.main()