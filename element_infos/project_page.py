from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.base_page import BasePage
from common.set_driver import set_driver
from common.conf_utils import conf
from common.element_data_utils import ElementDataUtils

class ProjectPage(BasePage):
    def __init__(self,driver):
       super().__init__(driver)
       elemrnts = ElementDataUtils('项目').get_element_info('project_page')
       self.task_menu =elemrnts['task_menu']
       self.kanban_menu =elemrnts['kanban_menu']
       self.burn_menu =elemrnts['burn_menu']
       self.list_menu =elemrnts['list_menu']
       self.story_menu =elemrnts['story_menu']
       self.qa_menu =elemrnts['qa_menu']
       self.doc_menu =elemrnts['doc_menu']
       self.team_menu =elemrnts['team_menu']
       self.action_menu =elemrnts['action_menu']
       self.product_menu =elemrnts['product_menu']
       self.view_menu =elemrnts['view_menu']

    def goto_task(self):  #进入任务
        self.click(self.task_menu)


if __name__ =='__main__':
    driver = set_driver(conf.get_chandao_path)
    project_page = ProjectPage(driver)
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    login_page.input_username('admin')
    login_page.input_password('Lrh19960912')
    login_page.click_login()
    main_page.goto_project()
    project_page.goto_task()