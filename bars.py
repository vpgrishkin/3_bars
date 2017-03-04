import json
import sys
import os
from math import hypot

DEFAULT_FILE_NAME = 'default.json'
DEFAULT_FILE_ENCODING = 'windows-1251'


def load_data(file_path, file_encoding):
    with open(file_path, 'r', encoding=file_encoding) as json_file:
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    get_closest_bar = min(data, key=lambda x: hypot(float(x['Longitude_WGS84']) - longitude, float(x['Latitude_WGS84']) - latitude))
    return get_closest_bar


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска!  Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))
            work_file = sys.argv[1]

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)
    
    data_from_json = load_data(work_file, DEFAULT_FILE_ENCODING)

    biggest_bar = get_biggest_bar(data_from_json)
    print('Самый большой бар: {}'.format(biggest_bar['Name']))
    
    smallest_bar = get_smallest_bar(data_from_json)
    print('Самый маленький бар: {}'.format(smallest_bar['Name']))
    
    longitude = float(input('Введите longitude:'))
    latitude = float(input('Введите latitude:'))
    closest_bar = get_closest_bar(data_from_json, longitude, latitude)
    print('Ближайший объект')
    print(closest_bar)