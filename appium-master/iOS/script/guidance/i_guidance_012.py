# -*- coding: utf-8 -*- 
import os
import unittest
import time

from ..config.configParam import *
from appium import webdriver
from ..common import common

class i_guidance_012(unittest.TestCase):
    def setUp(self):
        configParam = ConfigParam()
        self.driver = configParam.getwebdriver()

    def tearDown(self):
        self.driver.quit()

    # ID: Guidance-012
    # Des: 选择年龄标签后的跳转
    def guidance_012(self):

        # Wait新手引导首页
        common.wait_for(self.driver, u'-请选择登录方式-', 5)

        # 1.点击看看再说>>
        self.driver.find_element_by_accessibility_id('看看再说按钮').click()

        # 2.点击“男”icon
        maleIcon = self.driver.find_element_by_accessibility_id('gender_male_unselect')
        maleIcon.click()

        # 等待年龄标签页面加载
        time.sleep(2)

        # 3.点击“90后”
        self.driver.find_element_by_accessibility_id('90后').click()

        common.wait_for(self.driver, u'分类', 10)         

if __name__ == '__main__':
    unittest.main()