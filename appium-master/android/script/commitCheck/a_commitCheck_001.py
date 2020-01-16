# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common
from ..common import installApp

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class test_commitCheck_001(unittest.TestCase):
    def setUp(self):
        os.popen("adb uninstall 'fm.qingting.qtradio'")
        installApp.install()

        time.sleep(3)

        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: commitCheck-001
    # Des: 对提交的commit做最基本的case验证
    def commitCheck_001(self):

        time.sleep(2)
        # 切换到alert窗口(Access location)
        alert = self.driver.switch_to_alert()
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        # Step2: 新手引导
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("-请选择注册/登录方式-")', 1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("看看再说>>>")').click()
        self.driver.find_element_by_id('fm.qingting.qtradio:id/gender_male').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("-选择你的年龄标签-")')
        self.driver.find_element_by_id('fm.qingting.qtradio:id/age_90').click()
        common.wait_for_ByAndroidUiAutomator(self.driver, 'new UiSelector().text("分类")', 5)
        self.driver.find_element_by_accessibility_id('分类') 

        # 关闭首页弹窗
        time.sleep(2)
        self.driver.tap([(540,1565),(0,0)])

        # Step3: 搜索节目后播放并下载
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

        time.sleep(2)
        self.driver.tap([(550,850),(0,0)])
        time.sleep(2)
        self.driver.tap([(550,850),(0,0)])

        # Check播放
        pauseButton = self.driver.find_element_by_accessibility_id('playButton')

        # 点击播放页“更多”，并进入批量下载页面
        more = self.driver.find_element_by_accessibility_id('more_icon')
        more.click()

        # 点击“下载节目”
        downloadMore = self.driver.find_element_by_accessibility_id('download')
        downloadMore.click()

        # 下载第一个节目
        downloadFirstProgram = self.driver.find_element_by_id('fm.qingting.qtradio:id/iv_download_state')
        downloadFirstProgram.click()

        # 点击添加收藏弹窗上的“以后再说”
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("以后再说")').click()

        # 批量下载页进入我的下载
        myDownloadPage = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的下载")')
        myDownloadPage.click()  

        # 验证下载存在
        downloadedProgram = self.driver.find_element_by_android_uiautomator('new UiSelector().text("郭德纲 于谦")')
        self.assertIsNotNone(downloadedProgram) 

        # Step4: 删除已下载
        deleteButton = self.driver.find_element_by_accessibility_id('downloadedListView_0_delete')
        deleteButton.click()
        self.driver.switch_to_alert()
        self.driver.find_element_by_accessibility_id('warningDialog_confirm').click()

if __name__ == '__main__':
    unittest.main()