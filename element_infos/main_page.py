from element_infos.login_page import LoginPage
from common.element_data_utils import ElementDataUtils
from common.base_page import BasePage
from common.conf_utils import conf
from common.set_driver import set_driver

class MainPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)
       element = ElementDataUtils('项目').get_element_info('main_page')
       self.companyname_showbox = element['companyname_showbox']
       self.myzone_menu = element['myzone_menu']
       self.product_menu = element['product_menu']
       self.project_menu = element['project_menu']
       self.username_showspan = element['username_showspan']
       # print(self.companyname_showbox)

    def get_companyname(self,text):  #获取公司名称
        value = self.get_element_attribute(self.companyname_showbox,text)
        print(value)

    def goto_myzone(self):  #进入我的地盘
        self.click(self.myzone_menu)
    def goto_product(self):  #进入产品菜单
        self.click(self.product_menu)
    def goto_project(self):  #进入项目菜单
        self.click(self.project_menu)
    def get_usename(self):  #获取用户名
      value = self.text(self.username_showspan)
      print(value)


if __name__ =="__main__":
    driver = set_driver(conf.get_chandao_path)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    login_page.input_username('admin')
    login_page.input_password('Lrh19960912')
    login_page.click_login()
    main_page.get_companyname('title')
    main_page.goto_project()
    main_page.goto_product()
    main_page.get_usename()
