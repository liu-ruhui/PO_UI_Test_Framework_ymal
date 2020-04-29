
from common.base_page import BasePage
from common.set_driver import set_driver
from common.conf_utils import conf
from common.element_yaml_utils import read_yaml



class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@id="account"]',
        #                           'timeout':5}
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@name="password"]',
        #                           'timeout': 2}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//button[@id="submit"]',
        #                           'timeout': 2}
        # self.keeplogin_checkbox = {'element_name': '复选框：记住密码',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@name="keepLogin[]"]',
        #                           'timeout': 2}
        elemenets = read_yaml('login_page')
        self.username_inputbox = elemenets['username_inputbox']
        self.password_inputbox = elemenets['password_inputbox']
        self.login_button = elemenets['login_button']

    def input_username(self,username):  #方法 ==》控件的操作
        self.input(self.username_inputbox,username)

    def input_password(self,password):
        self.input(self.password_inputbox,password)

    def click_login(self):
       self.click(self.login_button)



if __name__ =='__main__':
    driver = set_driver(conf.get_chandao_path)
    login_page = LoginPage(driver)
    login_page.input_username(conf.get_username)
    login_page.input_password(conf.get_password)
    login_page.click_login()