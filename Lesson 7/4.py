#!/usr/bin/python3

import os

print(f'Имя операционной системы: {os.name}')
print(f'Имя пользователя, вошедшего в терминал: {os.getlogin()}')
print(f'Список файлов и директорий в папке:\n{os.listdir(r"C:/")}')