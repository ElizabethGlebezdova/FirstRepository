#!/usr/bin/python3

from math import sqrt
import cmath

print('ax^2 + bx + c = 0')
print('Нужно ли ввести комплексные коэффициенты?\n1. да\n2. нет')
while(True):
    isComplex = input()
    if (isComplex == '1' or isComplex == '2'):
        break
    print('Неверный ввод! Попробуйте еще раз!\n1. да\n2. нет')
match isComplex:
    case '1':
        print('Введите коэффициенты: ')
        a, b, c = complex(input('a = ')), complex(input('b = ')), complex(input('c = '))
        if (a == 0 and b == 0 and c == 0):
            print('x - любое число')
        elif (a == 0 and b == 0):
            print('Нет решений')
        elif (a == 0 and c == 0):
            print('x = 0')
        elif (a == 0):
            print('Находим корень:')
            x = -c / b
            print('x = -c / b = ', -c, ' / ', b, ' = ', x)
        else:
            print('Вычисляем дискриминант:')
            D = b**2 - 4 * a * c
            print('D = b^2 - 4ac = ', b, '^2 - 4*', a, '*', c, ' = ', D)
            if (D == 0):
                print('Находим корень: ')
                x = -b/(2*a)
                print('x = -b / 2a = ', -b, ' / 2*', a, ' = ', x)
            else:
                print('Находим корни: ')
                x1 = (-b + cmath.sqrt(D))/(2*a)
                print('x1 = (-b + sqrt(D)) / 2a = (', -b, ' + ', cmath.sqrt(D), ') / 2*', a, ' = ', x1)
                x2 = (-b - cmath.sqrt(D))/(2*a)
                print('x2 = (-b + sqrt(D)) / 2a = (', -b, ' + ', cmath.sqrt(D), ') / 2*', a, ' = ', x2)
    case '2':
        print('Введите коэффициенты: ')
        a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
        if (a == 0 and b == 0 and c == 0):
            print('x - любое число')
        elif (a == 0 and b == 0):
            print('Нет решений')
        elif (a == 0 and c == 0):
            print('x = 0')
        elif (a == 0):
            print('Находим корень:')
            x = -c / b
            print('x = -c / b = %.2f / %.2f = %.2f' % (-c, b, x))
        else:
            print('Вычисляем дискриминант:')
            D = b**2 - 4 * a * c
            print('D = b^2 - 4ac = %.2f^2 - 4*%.2f*%.2f = %.2f' % (b, a, c, D))
            if (D == 0):
                print('Находим корень: ')
                x = -b/(2*a)
                print('x = -b / 2a = %.2f / 2*%.2f = %.2f' % (-b, a, x))
            elif (D > 0):
                print('Находим корни: ')
                x1 = (-b + sqrt(D))/(2*a)
                print('x1 = (-b + sqrt(D)) / 2a = (%.2f + %.2f) / 2*%.2f = %.2f' % (-b, sqrt(D), a, x1))
                x2 = (-b - sqrt(D))/(2*a)
                print('x2 = (-b - sqrt(D)) / 2a = (%.2f - %.2f) / 2*%.2f = %.2f' % (-b, sqrt(D), a, x2))
            else:
                print('Находим корни: ')
                x1 = (-b + cmath.sqrt(D))/(2*a)
                print('x1 = (-b + sqrt(D)) / 2a = (%.2f' % (-b), ' + ', cmath.sqrt(D), ') / 2*%.2f' % (a), ' = ', x1)
                x2 = (-b - cmath.sqrt(D))/(2*a)
                print('x2 = (-b + sqrt(D)) / 2a = (%.2f' % (-b), ' + ', cmath.sqrt(D), ') / 2*%.2f' % (a), ' = ', x2)