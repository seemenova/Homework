# 1. Работа с HTML
# Скачать содержимое страницы https://epam.com с помощью requests
# Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4

import requests
from bs4 import BeautifulSoup

count = 0
response = requests.get("https://epam.com", verify = False)
if response.status_code == requests.codes.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    print('COUNT = ', len(soup.findAll('div')))

# 2. Базы данных
# Работа с sqlite.
# С помощью SQL запросов создать таблицу, содержащую 2 стобца: номер и имя
# Добавить три строки с данными.
# Получить данные из таблицы и распечатать их на экране.

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE testtable
             (number, name)''')
c.execute("INSERT INTO testtable VALUES (1, 'NAME1')")
c.execute("INSERT INTO testtable VALUES (2, 'NAME2')")
c.execute("INSERT INTO testtable VALUES (3, 'NAME3')")

conn.commit()

for row in c.execute('SELECT * FROM testtable ORDER BY number'):
        print(row)

conn.close()