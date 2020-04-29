import os
from selenium import webdriver
# from common.base_page import BasePage
from common.conf_utils import conf



def set_driver(url):
    currrent_path = os.path.dirname(__file__)
    driver_path = os.path.join(currrent_path, conf.get_gecko_path)
    driver= webdriver.Firefox(executable_path=driver_path)
    driver.maximize_window()
    driver.get(url)
    return driver




if __name__ =='__main__':
    set_driver(conf.get_chandao_path)

