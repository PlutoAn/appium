# -*- coding: utf-8 -*- 
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_download_008(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-008
    # Des: 播放页-更多，下载节目
    def download_008(self):   

        # wait app lanuched
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 30)
        self.downloadProgram(self.driver)

        # 验证下载存在
        downloadedProgram = self.driver.find_element_by_android_uiautomator('new UiSelector().text("郭德纲 于谦")')
        self.assertIsNotNone(downloadedProgram)

        common.deleteChannel(self.driver)

    # 下载节目
    def downloadProgram(self, driver):

        # click "搜索"，进入搜索页面
        search = self.driver.find_element_by_accessibility_id('输入收听内容')
        search.click() 

        # 搜索专辑并进入专辑页
        TypeTextField = self.driver.find_element_by_id('fm.qingting.qtradio:id/searchKey')
        TypeTextField.send_keys(u'郭德纲')
        self.driver.find_element_by_id('fm.qingting.qtradio:id/searchAction').click()

        common.wait_for_ByAccessibilityId(self.driver, 'CustomizedAdapter_0', 5)        
        searchList_0 = self.driver.find_element_by_accessibility_id('CustomizedAdapter_0')
        searchList_0.click()

        # 点击专辑第一个节目并进入播放页
        common.wait_for_ByAccessibilityId(self.driver, 'programList_0', 5)        
        channelProgram_0 = self.driver.find_element_by_accessibility_id('programList_0')
        channelProgram_0.click()

        # 点击播放页“更多”，并进入批量下载页面
        more = self.driver.find_element_by_accessibility_id('more_icon')
        more.click()

        # 点击“下载节目”
        downloadMore = self.driver.find_element_by_accessibility_id('download')
        downloadMore.click()

        # 下载第一个节目
        downloadFirstProgram = self.driver.find_element_by_id('fm.qingting.qtradio:id/iv_download_state')
        downloadFirstProgram.click()

        addcollect = common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("以后再说")', 2)
        
        if addcollect == 'True':
            # 点击添加收藏弹窗上的“以后再说”
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("以后再说")').click()

        # 批量下载页进入我的下载
        myDownloadPage = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的下载")')
        myDownloadPage.click()