"""
3. Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.
"""

import requests
import os.path
from os.path import abspath

def saveinfo(filename):
    path = "https://epam.com"
    try:
        r = requests.get(path, verify = False)
        u = r.text.encode('utf-8')
        f = open(filename, 'w',encoding="utf-8")
        f.write(r.text)
        f.close
        print("Данные с сайта {0} сохранены в файл {1}".format(path, os.path.abspath(filename)))
    except FileNotFoundError as fnfe:
        print("Файла не существует")
        print(fnfe)
    except UnicodeEncodeError as uee:
        print("Ошибка кодировки")
        print(uee)

if __name__ == '__main__':
    filename = input('Enter the name of final file: ')
    saveinfo(filename)