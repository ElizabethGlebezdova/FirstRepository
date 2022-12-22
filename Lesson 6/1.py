#!/usr/bin/python3

def strings_to_bytecodes(list):
    """Перевод списка строк в список байт кодов"""
    byteCodes = []
    for i in list:
        byteCodes.append(i.encode('utf-8'))
    return byteCodes

def bytecodes_to_strings(list):
    """Перевод списка байт кодов в список строк"""
    strings = []
    for i in list:
        strings.append(i.decode('utf-8'))
    return strings

list_of_str = []
str = input('Введите строки(конец - 0):\n')
while(str != '0'):
    list_of_str.append(str)
    str = input()
list_of_bytes = strings_to_bytecodes(list_of_str)
print(f'Список строк в список байт кодов:\n{list_of_bytes}')
print(f'Список байт кодов в список строк:\n{bytecodes_to_strings(list_of_bytes)}')