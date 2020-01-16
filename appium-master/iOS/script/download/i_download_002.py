# -*- coding: utf-8 -*- 
import os
import unittest

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_download_002(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-002
    # Des: “下载tab->已下载”页面无任何节目时默认图和提示信息显示正确，且“个人中心->我的下载“下方显示的数字为0
    def download_002(self):   

        # skip ad and wait app lanuched
        common.skip_ad(self.driver)
        common.wait_for(self.driver, u'分类', 10)

        # click "下载"tab
        download = self.driver.find_element_by_accessibility_id('下载')
        download.click() 

        # 已下载默认图验证
        downloadedDefault = self.driver.find_element_by_accessibility_id('暂无下载内容, 要离线收听，不耗流量？快把想听的内容下载下来吧')
        downloadedDefaultText = downloadedDefault.get_attribute('label')
        self.assertEqual(downloadedDefaultText, u'暂无下载内容, 要离线收听，不耗流量？快把想听的内容下载下来吧')        

if __name__ == '__main__':
    unittest.main()