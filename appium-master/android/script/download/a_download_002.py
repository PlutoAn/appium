# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_download_002(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-002
    # Des: “下载tab->已下载”页面无任何节目时默认图和提示信息显示正确，且“个人中心->我的下载“下方显示的数字为0
    def download_002(self):   

        # wait app lanuched
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 30)

        # 进入个人中心
        myUserCenter = self.driver.find_element_by_accessibility_id('我的')
        self.assertIsNotNone(myUserCenter)
        myUserCenter.click()

        # click "我的下载"
        download = self.driver.find_element_by_accessibility_id('我的下载')
        self.assertIsNotNone(download)
        download.click()

        # 已下载默认图验证
        downloadedDefault = self.driver.find_element_by_id('fm.qingting.qtradio:id/viewPager')       

if __name__ == '__main__':
    unittest.main()