#!/usr/bin/python3

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print('Сложение: %.2f + %.2f = %.2f' % (a, b, a + b))
print('Вычитание: %.2f - %.2f = %.2f' % (a, b, a - b))
print('Умножение: %.2f * %.2f = %.4f' % (a, b, a * b))
if (b != 0):
    print('Деление: %.2f / %.2f = %.2f' % (a, b, a / b))
print('Возведение в степень: %.2f^%.2f = %.2f' % (a, b, a ** b))
print('Возведение в степень: %.2f^%.2f = %.2f' % (b, a, b ** a))
if (b != 0):
    print('Деление по модулю: |%.2f / %.2f| = %.2f' % (a, b, a % b))
    print('Целочисленное деление: %.2f / %.2f = %.2f' % (a, b, a // b))