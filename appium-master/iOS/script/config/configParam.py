# -*- coding: utf-8 -*- 
import os
import json
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ConfigParam(object):
    configPath = "config.ini"

    def setConfigPath(self, path = "config.ini"):
        self.configPath = path

    def setReleaseParam(self):
        self.configPath = "releaseConfig.ini"

    #参数结构
    # {"command_executor": "http://127.0.0.1:4723/wd/hub",
    #  "desired_capabilities": {"automationName": "XCUITest", 
    #                           "app":PATH("../package/QTTourAppStore.ipa"),
    #                           "platformName": "iOS", 
    #                           "platformVersion": "10.3", 
    #                           "deviceName": "iPhone 6s", 
    #                           "udid": "1c232096187a6ced9e5d11d75f5d12d1bc6faf54"
    #                           "bundleId": "com.Qting.QTTour"}
    # }
    def getwebdriver(self):
        if os.path.exists(PATH(self.configPath)) == False :
            raise Exception('config is no exits')
        with open(PATH(self.configPath)) as f:
            load_dict = json.load(f)
            desired_capabilities = load_dict['desired_capabilities']
            if load_dict.get("desired_capabilities") == None :
                raise Exception('Miss required desired_capabilities')
            if desired_capabilities.get("automationName") == None :
                raise Exception('Miss required automationName')
            if desired_capabilities.get("platformName") == None :
                raise Exception('Miss required platformName')
            if desired_capabilities.get("platformVersion") == None :
                raise Exception('Miss required platformVersion')
            if desired_capabilities.get("deviceName") == None :
                raise Exception('Miss required deviceName')
            if desired_capabilities.get("bundleId") == None :
                raise Exception('Miss required bundleId')
            if desired_capabilities.get("app") != None :
                desired_capabilities['app'] = PATH(desired_capabilities['app'])
            driver = webdriver.Remote(
                command_executor=load_dict['command_executor'],
                desired_capabilities=load_dict['desired_capabilities'])
            return driver