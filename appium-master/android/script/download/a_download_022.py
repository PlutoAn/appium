# -*- coding: utf-8 -*- 
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class a_download_022(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Download-022
    # Des: 已下载专辑中点击“编辑”后，节目可以被选中
    def download_022(self):   

        # wait app lanuched
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 30)
        self.downloadProgram(self.driver)

        # 验证下载存在
        downloadedProgram = self.driver.find_element_by_android_uiautomator('new UiSelector().text("郭德纲 于谦")')
        self.assertIsNotNone(downloadedProgram)
        
        downloadedProgram.click()

        editButton = self.driver.find_element_by_accessibility_id('right_btn')
        editButton.click()

        cbSelected = self.driver.find_element_by_id('fm.qingting.qtradio:id/cb_selected')
        self.assertIsNotNone(cbSelected)
        selectAllbutton = self.driver.find_element_by_android_uiautomator('new UiSelector().text("全选")')
        self.assertIsNotNone(selectAllbutton)
        deleteButton = self.driver.find_element_by_android_uiautomator('new UiSelector().text("删除")')
        self.assertIsNotNone(deleteButton)
        
        self.driver.find_element_by_accessibility_id('left_btn').click()
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

        # 点击专辑第一个节目并下载
        common.wait_for_ByAccessibilityId(self.driver, 'programList_0', 5)        
        self.driver.find_element_by_accessibility_id('programList_0')
        downloadFirstProgram = self.driver.find_element_by_accessibility_id('programList_0_download')
        downloadFirstProgram.click()

        addcollect = common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("以后再说")', 2)    
        if addcollect == 'True':
            # 点击添加收藏弹窗上的“以后再说”
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("以后再说")').click()

        self.driver.find_element_by_accessibility_id('programList_1')
        downloadSecondProgram = self.driver.find_element_by_accessibility_id('programList_1_download')
        downloadSecondProgram.click()

        # 批量下载页进入我的下载
        self.driver.tap([(900,655),(0,0)])
        myDownloadPage = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的下载")')
        myDownloadPage.click()
