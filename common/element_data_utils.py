import os
import xlrd

current_path = os.path.dirname(__name__)
excel_path = os.path.join(current_path,'..//element_info_datas/element_infos.xlsx')
class ElementDataUtils:
    def __init__(self,page_name,element_path = excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_count = self.sheet.nrows
        self.col_count = self.sheet.ncols

    def get_element_info(self,pagename):
        element_infos = locals()
        for i in range(1, self.row_count):
            element_info = {}
            for j in range(1,self.col_count):
                cell_value = self.sheet.cell_value(i, j)
                cell_value = int(cell_value) if isinstance(cell_value,float)else str(cell_value)
                element_info[self.sheet.cell_value(0, j)] = cell_value
            if element_info['page'] == pagename:
                element_infos[self.sheet.cell_value(i, 0)] = {}
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__ =="__main__":
    try:
        elemenets = ElementDataUtils('项目').get_element_info('login_page')
        print(elemenets['keeplogin_checkbox'])
    except Exception as e:
        print('该页面无此参数')