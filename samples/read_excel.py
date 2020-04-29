import os
import xlrd


current_path = os.path.dirname(__name__)
excel_path = os.path.join(current_path,'..//element_info_datas/element_infos.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('login_page')
row_count = sheet.nrows
col_count = sheet.ncols

element_infos = locals()
for i in range(1,row_count):
    element_info = {}
    for j in range(1,col_count):
        # element_info[sheet.cell_value(0,j)] = {}
        element_info[sheet.cell_value(0,j)]= sheet.cell_value(i,j)
    if element_info['page'] == 'login_page':
        element_infos[sheet.cell_value(i,0)] = {}
        element_infos[sheet.cell_value(i,0)] = element_info

try:
   print(element_infos['keeplogin_checkbox'])
except Exception as e:
    print('该页面无此参数')
# print(element_infos['username_inputbox'])
