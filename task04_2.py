"""
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
"""

import logging
import os.path

from os import listdir
from os.path import isfile, join

def printfiles(path):
    try:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]     # Фильтруем каталоги, оставляем только файлы
        print(onlyfiles)
        logger.info("Path is {}".format(os.path.abspath(path)))
        logger.info("The number of files: {}".format(len(onlyfiles)))
    except FileNotFoundError as fnfe:
        logger.error("Path not found!")
        print(fnfe)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s -- %(levelname)s : %(message)s')
    logger = logging.getLogger(__name__)
    path = input('Enter the path: ')
    printfiles(path)
