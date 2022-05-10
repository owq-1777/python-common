# -*- coding: utf-8 -*-
'''
@Desc   :   文件IO操作
'''


import glob
import inspect
import json
import os
import re
import yaml  # pip install pyyaml
import pandas as pd

from PIL import Image, ImageGrab    # linix: pip install pillow


# ------------------------------------  ------------------------------------ #

def get_run_filename():
    """ 获取当前执行文件名 不含后缀 """
    return os.path.basename(inspect.stack()[1][1]).split('.')[0]

def get_files_path(search_dir, full_path: bool = True, filter=False):
    """ 获取目录下文件路径

    :param search_dir: 搜索目录路径
    :param full_path: 是否获取完整路径
    :param filter: 正则表达式过滤
    :return 路径列表
    """

    files_path = []

    for dir_path, dir_names, file_names in os.walk(search_dir):
        for file_name in file_names:
            if filter and not re.search(filter, file_name):
                continue
            if full_path:
                files_path.append(os.path.join(dir_path, file_name))
            else:
                files_path.append(file_name)

    return files_path


# ------------------------------------ File ------------------------------------ #

def load_file(filename, coding='UTF-8') -> str:
    """ 获取文件文本数据 只支持utf-8和gbk编码文件 """

    with open(filename, 'r', encoding=coding) as f:
        return f.read()


# ------------------------------------ Json ------------------------------------ #

def load_json(filename:str, conding:str='UTF-8') -> dict:
    """Load .json file"""
    with open(filename, mode='r', encoding=conding) as f:
        data = json.load(f)
    return data

def save_json(data, filename:str, conding:str='UTF-8'):
    """ Save the data to a JSON file """
    if filename.split('.')[-1] == filename:
        filename += '.json'
    with open(filename, mode='w', encoding=conding) as f:
        json.dump(data, fp=f)

# ------------------------------------ YML ------------------------------------ #

def load_yml(conf_path:str, conding:str='UTF-8') -> dict:
    """Load .yml file """
    with open(file=conf_path, mode='r', encoding=conding) as f:
        return yaml.load(stream=f, Loader=yaml.FullLoader)

def save_yml(data, filename:str, conding:str='UTF-8'):
    """ Save the data to a YML file """
    if filename.split('.')[-1] == filename:
        filename += '.yml'
    with open(filename, mode='w', encoding=conding) as f:
        yaml.dump(data, stream=f)

def load_yml_dir(conf_dir:str) -> dict:
    """ Load all YML configurations in the directory """

    conf = {}
    for file_path in glob.glob(os.path.join(conf_dir, '*.yml')):
        conf_obj = load_yml(file_path)
        conf_name = os.path.splitext(os.path.basename(file_path))[0]
        conf[conf_name] = conf_obj

    return conf


# ------------------------------------ Paste ------------------------------------ #

def save_paste_pic(filename: str) -> bool:
    """ Save the clipboard picture """
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        im.save(filename)
        return True
    return False

def json2csv(data: list[dict], filename: str = 'data', encoding='utf_8'):
    """ json数据转存到csv

    :param data: JSON数据
    :param filename: CSV文件名
    """

    filename = filename if filename[-4:] == '.csv' else f'{filename}.csv'

    format_data = [{k: json.dumps(v, ensure_ascii=False).replace(',', ' ').replace('\n', ' ') for k, v in item.items()} for item in data]
    dataframe = pd.DataFrame(format_data)

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    if os.path.exists(filename):
        dataframe.to_csv(filename, mode='a', encoding=encoding, index=False, index_label=False, sep=',', header=False)
    else:
        dataframe.to_csv(filename, mode='a', encoding=encoding, index=False, index_label=False, sep=',')

def csv2xlsx(csv_dir):
    csv = pd.read_csv(csv_dir, encoding='utf-8')
    csv.to_excel(f'{csv_dir[:-4]}.xlsx', sheet_name='data')

if __name__ == '__main__':
    data = {
        'a': 2,
        'a2': 1,
        '1343': 1,
        'fa': [1,3,14,1,1],
        'd': {
            '1': '12',
            '2': "12"
        }
    }
    # data = [21,31,31]

    r = save_yml(data, 'ts.json')
    print(r)