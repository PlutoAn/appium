# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_commitCheck_001(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        configParam.setReleaseParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: commitCheck-001
    # Des: 对提交的commit做最基本的case验证
    def commitCheck_001(self):

        # Step1: allow alert
        time.sleep(2)

        # 切换到alert窗口(Access location)
        self.driver.switch_to_alert()
        ele = common.wait_for(self.driver, u'允许“蜻蜓FM”在您使用该应用时访问您的位置吗？', 3)
        if ele != 'False':
            alert = self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="允许“蜻蜓FM”在您使用该应用时访问您的位置吗？"]')
            allowButton = self.driver.find_element_by_accessibility_id('允许')
            allowButton.click()

        time.sleep(2)
        # 切换到alert窗口(Send notifiCations)
        self.driver.switch_to_alert()
        # alert = self.driver.find_element_by_xpath('//XCUIElementTypeAlert[@name="“蜻蜓FM” Would Like to Send You Notifications"]')
        allowButton = self.driver.find_element_by_accessibility_id('允许')
        allowButton.click()

        # Step2: 新手引导
        common.wait_for(self.driver, u'-请选择登录方式-', 5)
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()
        self.driver.find_element_by_accessibility_id('gender_male_unselect').click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id('80后').click()

        common.wait_for(self.driver, u'分类', 10)

        # Step3: 搜索节目后播放并下载
        search = self.driver.find_element_by_accessibility_id('我要搜索')
        search.click() 

        # 搜索专辑并进入专辑页
        TypeTextField = self.driver.find_element_by_xpath('//XCUIElementTypeTextField')
        TypeTextField.set_value(u'郭德纲')
        time.sleep(1)
        self.driver.find_element_by_accessibility_id('Search').click()

        common.wait_for(self.driver, 'list_0_0', 5)
        searchList_1 = self.driver.find_element_by_accessibility_id('list_0_0')
        searchList_1.click()

        # 点击专辑第一个节目并进入播放页
        common.wait_for(self.driver, 'list_0_0', 5)
        channelProgram_1 = self.driver.find_element_by_accessibility_id('list_0_0')
        channelProgram_1.click()

        # Check播放
        common.wait_for(self.driver, '更多', 5)
        common.wait_for(self.driver, '暂停', 5)
        pauseButton = self.driver.find_element_by_accessibility_id('暂停')
        pauseText = pauseButton.get_attribute('name')
        self.assertEqual(pauseText, u'暂停')

        # 点击播放页“更多”，并进入批量下载页面
        more = self.driver.find_element_by_accessibility_id('更多')
        more.click()

        # 点击“下载节目”
        downloadMore = self.driver.find_element_by_accessibility_id('下载节目')
        downloadMore.click()

        # 下载第一个节目
        downloadFirstProgram = self.driver.find_element_by_accessibility_id('list_0_download_addtolist')
        downloadFirstProgram.click()

        common.wait_for(self.driver, '进行中', 10)

        # 批量下载页进入我的下载
        myDownloadPage = self.driver.find_element_by_accessibility_id('我的下载')
        myDownloadPage.click()  

        # 验证下载存在
        downloadedProgram = self.driver.find_element_by_accessibility_id('list_0')
        self.assertIsNotNone(downloadedProgram) 

        # Step4: 删除已下载
        deleteButton = self.driver.find_element_by_accessibility_id('list_0_delete')
        deleteButton.click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_accessibility_id('确定').click()

if __name__ == '__main__':
    unittest.main()