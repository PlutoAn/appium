# -*- coding: utf-8 -*- 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wait for an element is displayed
def wait_for(driver, element, timeout):

    try:
        is_display = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, element)))
    except:
        is_display = ''

    if '' != is_display:
        isElementFind = 'True'
    else:
        isElementFind = 'False'

    return isElementFind

# 跳过广告
def skip_ad(driver):

    if wait_for(driver, u'跳过广告', 5) == 'True':

        # 点击跳过广告
        skipAdButton = driver.find_element_by_accessibility_id(u'跳过广告')
        skipAdButton.click()
    elif wait_for(driver, 'btn single close nm', 5) == 'True':
        
        # 点击跳过广告
        skipAdButton = driver.find_element_by_accessibility_id('btn single close nm')
        skipAdButton.click()
