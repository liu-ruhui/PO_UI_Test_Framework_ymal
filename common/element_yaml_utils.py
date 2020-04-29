import os
import yaml

current_path = os.path.dirname(__file__)
yaml_path = os.path.join(current_path, '..//element_info_datas/element_infos.yaml')



def read_yaml(page_name,element_path=yaml_path):
    file = open(element_path, 'r', encoding='utf-8')
    yaml_content = file.read()
    dict_yaml= yaml.safe_load(yaml_content)
    elements = dict_yaml[page_name]
    return elements

if __name__ == '__main__':
    e = read_yaml('login_page')
    print(e)



