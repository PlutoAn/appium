# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_download_005(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-005
    # Des: 点击tab“下载”，能够成功进入“我的下载”页面，且包含“已下载”和“正在下载”两个tab
    def download_005(self):

        # skip ad and wait app lanuched
        common.skip_ad(self.driver)
        common.wait_for(self.driver, u'分类', 10)

        # click "下载"tab'
        download = self.driver.find_element_by_accessibility_id('下载')
        self.assertIsNotNone(download)
        download.click()

        # 我的下载页-title
        downloadPageTitleObject = self.driver.find_element_by_accessibility_id('我的下载')
        downloadPageTitle = downloadPageTitleObject.get_attribute('name')
        self.assertEqual(downloadPageTitle, u'我的下载')


        # 验证“已下载”tab
        downloadedTabObject = self.driver.find_element_by_accessibility_id('已下载')
        downloadedTabTitle = downloadedTabObject.get_attribute('label')
        self.assertEqual(downloadedTabTitle, u'已下载')


        # 验证“正在下载”tab
        downloadingTabObject = self.driver.find_element_by_accessibility_id('正在下载')
        downloadingTabTitle = downloadingTabObject.get_attribute('label')
        self.assertEqual(downloadingTabTitle, u'正在下载')       

if __name__ == '__main__':
    unittest.main()