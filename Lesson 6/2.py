#!/usr/bin/python3

alcMolDict = dict()
count = 0
try:
    with open('Lesson 6\Input.txt', 'r') as file:
        alcMolDict['C'] = int(file.readline())
        alcMolDict['H'] = int(file.readline())
        alcMolDict['O'] = int(file.readline())
    while ((alcMolDict['C'] - 2 >= 0) and
           (alcMolDict['H'] - 6 >= 0) and 
           (alcMolDict['O'] - 1 >= 0)):
            count += 1
            alcMolDict['C'] -= 2
            alcMolDict['H'] -= 6
            alcMolDict['O'] -= 1
    with open('Lesson 6\Output.txt', 'w') as file:
        file.write(f'The maximum possible number of alcohol molecules that can be obtained from the atoms represented in the input data: {count}')
        print(f'The maximum possible number of alcohol molecules that can be obtained from the atoms represented in the input data: {count}')
except FileNotFoundError:
    print('Ошибка: файл не найден!')
except ValueError:
    print('Ошибка: в файле даны неверные данные!')