#!/usr/bin/python3

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print('%.2f + %.2f = %.2f' % (a, b, a + b))
print('%.2f - %.2f = %.2f' % (a, b, a - b))
print('%.2f * %.2f = %.4f' % (a, b, a * b))
if (b != 0):
    print('%.2f / %.2f = %.2f' % (a, b, a / b))
print('%.2f^%.2f = %.2f' % (a, b, a ** b))
print('%.2f^%.2f = %.2f' % (b, a, b ** a))
print('Деление по модулю: |%.2f / %.2f| = %.2f' % (a, b, abs(a / b)))
print('Целочисленное деление: %.2f / %.2f = %.2f' % (a, b, int(a // b)))