import os
import yaml

current_path = os.path.dirname(__file__)
yaml_path = os.path.join(current_path, '..\\element_info_datas\element_infos.yaml')



class ElementYamlData:
    def __init__(self, page_name, element_path=yaml_path):
        self.page_name =page_name
        # 读出yaml文件
        self.file = open(element_path, 'r', encoding='utf-8')
        self.yaml_content = self.file.read()

    def read_yaml(self):
        dict_yaml = yaml.safe_load(self.yaml_content)
        elements = dict_yaml[self.page_name]
        return elements

if __name__ == '__main__':
   e = ElementYamlData('login_page').read_yaml()
   print(e)



