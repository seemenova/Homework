"""
1. Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.
"""

import click
import subprocess

@click.command()
@click.argument('filename')

def openfile(filename):
    try:
        subprocess.run(filename)
    except FileNotFoundError as fnfe:
        print("The executable file is not exist!")  # Обрабатываем неправильное или несуществующее имя
        print(fnfe)
    except OSError as ose:
        print("The specified file is not an application")  # Обрабатываем ввод не исполняемого файла
        print(ose)
    except Exception as e:
        print(e)
    else:
        print("All ok! The executable file is closed")


if __name__ == '__main__':
    openfile()
