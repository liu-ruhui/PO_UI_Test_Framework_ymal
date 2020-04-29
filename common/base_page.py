import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.conf_utils import conf
from selenium.webdriver.support import expected_conditions as EC

from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

     #浏览器操作封装 -->二次封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址 %s'%url)
    def set_maxwindow(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')
    def set_minwindow(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')
    def refresh(self):
        logger.info('浏览器刷新操作')
    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value
    def close(self):
        value = self.driver.close()
        logger.info('关闭当前页面')
        return value

    #元素操作封装
    #element_info = {'element_name': '登录按钮','locator_type': 'xpath', 'locator_value': '//input[@name="keepLogin[]"]', 'timeout': 5}
    def find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_time = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver,locator_time)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        # element = WebDriverWait(self.driver,locator_time)\
        #     .until(EC.presence_of_element_located(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        return element

#元素点击操作
    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作' % element_info['element_name'])
#元素输入内容
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s'%(element_info['element_name'],content))

#获取某个元素(title)的值
    def get_element_attribute(self, element_info, content):
        element = self.find_element(element_info)
        value = element.get_attribute(content)
        # element.getattribute(content)
        logger.info('[%s]元素查找%s的值:%s' % (element_info['element_name'], content,value))
        return value

#获取文本值
    def text(self, element_info):
        element = self.find_element(element_info)
        value=element.text
        logger.info('[%s]元素获取文本值:%s' % (element_info['element_name'], value))
        return value