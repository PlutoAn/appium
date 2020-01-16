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

class a_download_018(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-018
    # Des: 主页点击“下载”tab进入我的下载页面。
    def download_018(self):

        # 跳过广告和启动app
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 30)
        
        # 进入个人中心
        downLoad = self.driver.find_element_by_accessibility_id('下载')
        self.assertIsNotNone(downLoad)
        downLoad.click()

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