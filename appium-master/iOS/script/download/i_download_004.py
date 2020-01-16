# -*- coding: utf-8 -*- 
import unittest

from ..config.configParam import *
from time import sleep
from appium import webdriver
from ..common import common

class i_download_004(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-004
    # Des: 播放页下载
    def download_004(self):   

        # skip ad and wait app lanuched
        common.skip_ad(self.driver)
        common.wait_for(self.driver, '分类', 10)
        self.downloadProgram(self.driver)

        # 验证下载存在
        downloadedProgram = self.driver.find_element_by_accessibility_id('list_0')
        self.assertIsNotNone(downloadedProgram)

        self.deleteChannel(self.driver)

    # 下载节目
    def downloadProgram(self, driver):

        # click "搜索"，进入搜索页面
        search = driver.find_element_by_accessibility_id('我要搜索')
        search.click() 

        # 搜索专辑并进入专辑页
        TypeTextField = driver.find_element_by_xpath('//XCUIElementTypeTextField')
        TypeTextField.set_value(u'郭德纲')
        sleep(1)
        driver.find_element_by_accessibility_id('Search').click()

        common.wait_for(driver, 'list_0_0', 5)
        searchList_1 = driver.find_element_by_accessibility_id('list_0_0')
        searchList_1.click()

        # 点击专辑第一个节目并进入播放页
        common.wait_for(driver, 'list_0_0', 5)
        channelProgram_1 = driver.find_element_by_accessibility_id('list_0_0')
        channelProgram_1.click()

        # 点击播放页“更多”，并进入批量下载页面
        common.wait_for(driver, '更多', 5)
        more = driver.find_element_by_accessibility_id('更多')
        more.click()

        # 点击“下载节目”
        downloadMore = driver.find_element_by_accessibility_id('下载节目')
        downloadMore.click()

        # 下载第一个节目
        downloadFirstProgram = driver.find_element_by_accessibility_id('list_0_download_addtolist')
        downloadFirstProgram.click()

        common.wait_for(driver, '进行中', 10)

        # 批量下载页进入我的下载
        myDownloadPage = driver.find_element_by_accessibility_id('我的下载')
        myDownloadPage.click()


    # 删除已下载节目
    def deleteChannel(self, driver):

        # 删除已下载
        deleteButton = driver.find_element_by_accessibility_id('list_0_delete')
        deleteButton.click()

        #切换到alert窗口
        driver.switch_to_alert()
        driver.find_element_by_accessibility_id('确定').click()
