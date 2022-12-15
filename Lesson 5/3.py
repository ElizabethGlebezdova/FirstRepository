#!/usr/bin/python3

def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while(True):
    try:
        n = int(input('Введите номер числа Фибоначчи: '))
        fib = fibonacci(n)
        break
    except ValueError:
        print('Неверный ввод, попробуйте еще раз!')
    except RecursionError:
        print('Число не может быть отрицательным, попробуйте еще раз!')
print('Заданное число Фибоначчи равно', fib)