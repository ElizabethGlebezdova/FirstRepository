#!/usr/bin/python3

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while(True):
    try:
        n = int(input('Введите номер числа Фибоначчи: '))
        break
    except ValueError:
        print('Неверный ввод, попробуйте еще раз!')
print('Заданное число Фибоначчи равно', fibonacci(n))