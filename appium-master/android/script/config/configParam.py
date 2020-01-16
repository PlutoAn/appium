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
    #  "desired_capabilities": {"appPackage": "fm.qingting.qtradio", 
    #                           "app":PATH("../package/app-debug.apk"),
    #                           "platformName": "android", 
    #                           "appActivity": ".QTRadioActivity", 
    #                           "platformVersion": "6.0", 
    #                           "deviceName": "PJWWMZDQHE7SLRIJ"}
    # }
    def getwebdriver(self):
        if os.path.exists(PATH(self.configPath)) == False :
            raise Exception('config is no exits')
        with open(PATH(self.configPath)) as f:
            load_dict = json.load(f)
            desired_capabilities = load_dict['desired_capabilities']
            if load_dict.get("desired_capabilities") == None :
                raise Exception('Miss required desired_capabilities')
            if desired_capabilities.get("appPackage") == None :
                raise Exception('Miss required appPackage')
            if desired_capabilities.get("noReset") == None :
                raise Exception('Miss required noReset')
            if desired_capabilities.get("platformName") == None :
                raise Exception('Miss required platformName')
            if desired_capabilities.get("platformVersion") == None :
                raise Exception('Miss required platformVersion')
            if desired_capabilities.get("deviceName") == None :
                raise Exception('Miss required deviceName')
            if desired_capabilities.get("app") != None :
                desired_capabilities['app'] = PATH(desired_capabilities['app'])
            driver = webdriver.Remote(
                command_executor=load_dict['command_executor'],
                desired_capabilities=load_dict['desired_capabilities'])
            return driver