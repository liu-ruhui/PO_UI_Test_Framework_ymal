import os,time
from selenium import webdriver
from element_infos.project_page import ProjectPage
from common.login_utils import login
from element_infos.main_page import MainPage
from common.base_page import BasePage

class TaskPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)

       self.start = {'element_name': '开始按钮',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@title="开始"]',
                                 'timeout': 2}
       self.over = {'element_name': '完成',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@title="完成"]',
                                 'timeout': 2}
       self.work_time = {'element_name': '工时',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@title="工时"]',
                                 'timeout': 2}
       self.write_task = {'element_name': '编辑任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@title="编辑任务"]',
                                 'timeout': 2}
       self.little_task = {'element_name': '子任务',
                                 'locator_type': 'xpath',
                                 'locator_value':'//a[@title="子任务"]',
                                 'timeout': 2}



    def click_start(self):
        self.click(self.start)
    def click_over(self):
        self.click(self.over)
    def click_work_time(self):
        self.click(self.work_time)
    def click_write_task(self):
        self.click(self.write_task)
    def click_write_task(self):
        self.click(self.little_task)




if __name__ =='__main__':
   pass
