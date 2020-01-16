# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_download_003(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-003
    # Des: “下载tab->正在下载”页面无任何节目时默认图和提示信息显示正确
    def download_003(self):   

        # skip ad and wait app lanuched
        common.skip_ad(self.driver)
        common.wait_for(self.driver, u'分类', 10)

        # click "下载"tab
        download = self.driver.find_element_by_accessibility_id('下载')
        download.click() 

        # click“正在下载”tab
        downloadingTabObject = self.driver.find_element_by_accessibility_id('正在下载')
        downloadingTabObject.click()

        # 正在下载默认图验证
        downloadedDefault = self.driver.find_element_by_accessibility_id('暂无下载内容, 要离线收听，不耗流量？快把想听的内容下载下来吧')
        downloadedDefaultText = downloadedDefault.get_attribute('label')
        self.assertEqual(downloadedDefaultText, u'暂无下载内容, 要离线收听，不耗流量？快把想听的内容下载下来吧')

if __name__ == '__main__':
    unittest.main()