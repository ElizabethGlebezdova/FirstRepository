#!/usr/bin/python3

def stringsToBytecodes(list):
    byteCodes = []
    for i in list:
        byteCodes.append(i.encode('utf-8'))
    return byteCodes

def bytecodesToStrings(list):
    strings = []
    for i in list:
        strings.append(i.decode('utf-8'))
    return strings

listOfStr = []
str = input('Введите строку(конец - 0):\n')
while(str != '0'):
    listOfStr.append(str)
    str = input()
listOfBytes = stringsToBytecodes(listOfStr)
print(f'Список строк в список байт кодов:\n{listOfBytes}')
print(f'Список байт кодов в список строк:\n{bytecodesToStrings(listOfBytes)}')