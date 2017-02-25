# Ближайшие бары. Задача #3

На сайте data.mos.ru есть много разных данных, в том числе список московских баров (https://data.mos.ru/opendata/7710881420-bary). Его можно скачать в формате json.

Требуется написать скрипт, который рассчитает:
самый большой бар;
самый маленький бар;
самый близкий бар (текущие gps-координаты ввести с клавиатуры).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5, default.json, который можно скачать с https://data.mos.ru/opendata/7710881420-bary. Можно указать другое имя файла, указав его при запуске.

Запуск на Linux:

```#!bash

$ python3 bars.py # possibly requires call of python3 executive instead of just python
# Загружен файл default.json
Введите коодинаты longitude:1
Введите коодинаты latitude:1
Ближащий объект
{'Name': 'Staropramen', 'AdmArea': 'Центральный административный округ', 'IsNetObject': 'нет', 'Address': 'Садовая-Спасская улица, дом 19, корпус 1', 'ID': '00146638', 'Latitude_WGS84': '55.3033000000000000', 'global_id': 281494712, 'PublicPhone': [{'global_id': 34992.0, 'global_object_id': 281494712.0, 'system_object_id': '00146638 _1', 'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'TypeObject': 'бар', 'geoData': {'type': 'Point', 'coordinates': [36.900000000253, 55.303299999814]}, 'system_object_id': '00146638', 'Longitude_WGS84': '36.9000000000000000', 'District': 'Красносельский район', 'SocialPrivileges': 'нет'}


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
