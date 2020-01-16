# -*- coding: utf-8 -*- 
import os
import unittest
import time

from appium import webdriver
from ..config.configParam import *
from ..common import common

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class a_download_001(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-001
    # Des: 进入个人中心点击“我的下载”，能够成功进入“我的下载”页面，且包含“已下载”和“正在下载”两个tab
    def download_001(self):

        # 跳过广告和启动app
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 30)
        
        # 进入个人中心
        myUserCenter = self.driver.find_element_by_accessibility_id('我的')
        self.assertIsNotNone(myUserCenter)
        myUserCenter.click()

        # click "我的下载"
        download = self.driver.find_element_by_accessibility_id('我的下载')
        self.assertIsNotNone(download)
        download.click()

        # 我的下载页-title
        downloadPageTitleObject = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的下载")')

        # 验证“已下载”tab
        downloadedTabObject = self.driver.find_element_by_accessibility_id('已下载')
        downloadedTabTitle = downloadedTabObject.get_attribute('text')
        self.assertEqual(downloadedTabTitle, u'已下载')


        # 验证“正在下载”tab
        downloadingTabObject = self.driver.find_element_by_accessibility_id('正在下载')
        downloadingTabTitle = downloadingTabObject.get_attribute('text')
        self.assertEqual(downloadingTabTitle, u'正在下载') 

if __name__ == '__main__':
    unittest.main()