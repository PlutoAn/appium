# -*- coding: utf-8 -*- 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# wait for an element is displayed
def wait_for_ByAndroidUiAutomator(driver, element, timeout):

    try:
        is_display = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, element)))
    except:
        is_display = ''

    if '' != is_display:
        isElementFind = 'True'
    else:
        isElementFind = 'False'

    return isElementFind

def wait_for_ByAccessibilityId(driver, element, timeout):
    try:
        is_display = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, element)))
    except:
        is_display = ''

    if '' != is_display:
        isElementFind = 'True'
    else:
        isElementFind = 'False'

    return isElementFind

# 删除已下载节目
def deleteChannel(driver):

    # 删除已下载
    deleteButton = driver.find_element_by_accessibility_id('downloadedListView_0_delete')
    deleteButton.click()

    #切换到alert窗口
    driver.switch_to_alert()
    driver.find_element_by_accessibility_id('warningDialog_confirm').click()


