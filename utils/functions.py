import json


def open_file(file_json):
    """достаем файлы из json"""
    with open(file_json, 'r', encoding='utf-8') as file:
        goods = json.load(file)
        return goods
