#!/usr/bin/python3

from random import randint

set1, set2 = set(), set()
n1 = int(input('Введите размер первого набора: '))
n2 = int(input('Введите размер второго набора: '))

print('\nЗаполняем первый набор:')
for i in range(n1):
    set1.add(randint(0,20)) 
print(set1)

print('\nЗаполняем второй набор:')
for i in range(n2):
    set2.add(randint(0,20)) 
print(set2)

print(
    '\nЭлементы, которые входят одновременно в оба набора:',
    set1.intersection(set2))
print(
    'Элементы, которые входят только в первое, но не входят во второе:',
    set1.difference(set2))
print(
    'Элементы, которые входят только во второе, но не входят в первое:', 
    set2.difference(set1))
print(
    'Элементы, которые входят в первое или во второе, но не в оба из них одновременно:', 
    set1.symmetric_difference(set2))