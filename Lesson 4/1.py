#!/usr/bin/python3

from random import randint

lst = list()
n = int(input('Введите размер списка: '))
for i in range (n):
    lst.append(randint(0,99))
print('Заполнили список случайными числами:\n', lst)

print('Сортировка методом пузырька:')
for i in range(n-1):
    for j in range(n-i-1):
        if(lst[j] > lst[j+1]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
            print(lst)
print('\nОтсортированный список:', lst)