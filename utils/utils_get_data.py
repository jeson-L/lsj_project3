import json
import logging

import yaml


def utils_get_json_data(filename):
    list_data = []
    with open('./data/{}'.format(filename), 'r', encoding='utf-8') as f:
        for key, value in json.load(f).items():
            list_data.append(value)
        logging.info('读取到文件数据为：{}'.format(list_data))
        return list_data


def utils_get_yaml_data(filename, cd):
    list1 = []
    with open('./data/{}'.format(filename), 'r', encoding='utf-8') as f:
        for i in yaml.full_load(f)[cd].values():
            list1.append(i)
        logging.info('读取到文件数据为：{}'.format(list1))
        return list1


