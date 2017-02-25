DEFAULT_FILE_NAME = 'default.json'


def load_data(file_path):
	import json


	dict_from_json = None
	
	try:
		file = open(file_path, 'r', encoding='windows-1251')
	except Exception:
		print(u'Не удалось открыть файл')
		sys.exit(1)

	try:
		text = file.read()
	except Exception:
		print('Ошибка. Не удалось загрузить файл.')
	else:
		print('Загружен файл {}'.format(file_path))
	finally:
		file.close()

	dict_from_json = json.loads(text)
	return dict_from_json


def get_biggest_bar(data):
	biggest_bar = max(data, key=lambda x: x['SeatsCount'])
	return biggest_bar
	


def get_smallest_bar(data):
	smallest_bar = min(data, key=lambda x: x['SeatsCount'])
	return smallest_bar


def get_closest_bar(data, longitude, latitude):
# for perfectionists https://pypi.python.org/pypi/haversine
	from math import hypot
	get_closest_bar = min(data, key=lambda x: hypot(float(x['Longitude_WGS84']) - longitude, float(x['Latitude_WGS84']) - latitude))
	return get_closest_bar

if __name__ == '__main__':
	import sys
	import os
	
	if len(sys.argv) == 1:
		print('Нет параметров для запуска!  Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
		work_file = DEFAULT_FILE_NAME
	else:
		if os.path.isfile(work_file):
			print('Рабочий файл: ' + work_file)
			work_file = sys.argv[1]

	
	data_from_json = load_data(work_file)

	get_biggest_bar(data_from_json)
	get_smallest_bar(data_from_json)
	
	longitude = float(input('Введите longitude:'))
	latitude = float(input('Введите latitude:'))
	closest_bar = get_closest_bar(data_from_json, longitude, latitude)
	print('Ближайший объект')
	print(closest_bar)