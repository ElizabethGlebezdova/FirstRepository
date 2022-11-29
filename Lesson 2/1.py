#!/usr/bin/python3

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print('%f + %f = %f' % (a, b, a + b))
print('%f - %f = %f' % (a, b, a - b))
print('%f * %f = %f' % (a, b, a * b))
if (b != 0):
    print('%f / %f = %f' % (a, b, a / b))
print('%f^%f = %f' % (a, b, a ** b))
print('%f^%f = %f' % (b, a, b ** a))
print('Деление по модулю: |%f / %f| = %f' % (a, b, abs(a / b)))
print('Целочисленное деление: %f / %f = %f' % (a, b, int(a // b)))