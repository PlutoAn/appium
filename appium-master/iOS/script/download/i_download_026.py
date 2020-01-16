# -*- coding: utf-8 -*- 
import unittest

from ..config.configParam import *
from time import sleep
from appium import webdriver
from ..common import common

class i_download_026(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-026
    # Des: 进入有微社区的专辑页面查看“批量下载”按钮
    def download_026(self):   

        # skip ad and wait app lanuched
        common.skip_ad(self.driver)
        common.wait_for(self.driver, '分类', 5)

        # click "我的搜索"，进入搜索页面
        search = self.driver.find_element_by_accessibility_id('我要搜索')
        search.click() 

        # 搜索专辑并进入专辑页
        TypeTextField = self.driver.find_element_by_xpath('//XCUIElementTypeTextField')
        TypeTextField.set_value(u'张召忠开讲')
        sleep(1)
        self.driver.find_element_by_accessibility_id('Search').click()

        common.wait_for(self.driver, 'list_0_0', 5)
        searchList_1 = self.driver.find_element_by_accessibility_id('list_0_0')
        self.assertIsNotNone(searchList_1 )
        searchList_1.click()

        # 进入有微社区的专辑，查看“批量下载”按钮，点击后能够进入批量下载页面
        common.wait_for(self.driver, 'list_0_0', 5)
        bulkDownloadButton = self.driver.find_element_by_accessibility_id('grid_1')
        self.assertIsNotNone(bulkDownloadButton)
        bulkDownloadButton.click()
        bulkDownloadPage = self.driver.find_element_by_accessibility_id('张召忠开讲')
        self.assertIsNotNone(bulkDownloadPage)
        self.driver.find_element_by_accessibility_id('返回').click()

        # 检查收藏、分享、VIP社区按钮存在
        favoritesButton = self.driver.find_element_by_accessibility_id('grid_0')
        self.assertIsNotNone(favoritesButton)
        shareButton = self.driver.find_element_by_accessibility_id('grid_2')
        self.assertIsNotNone(shareButton)
        VIPButton = self.driver.find_element_by_accessibility_id('grid_3')
        self.assertIsNotNone(shareButton)





       


    

