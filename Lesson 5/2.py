#!/usr/bin/python3

def sum():
    sum = 0
    while True:
        try:
            n = float(input('Введите параметр: '))
            sum += n
        except ValueError:
            print('Вводите только числа!')
            sum += 0
        print('Сумма = %.2f' % sum)

sum()