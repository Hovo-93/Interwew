"""
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import sys
import os


def print_directory_contents(sPath):
    for name in os.listdir(sPath):
        name = os.path.abspath(sPath) + " " + name
        print(name)
        if os.path.isdir(name):
            print_directory_contents(name)


print_directory_contents('venv')
