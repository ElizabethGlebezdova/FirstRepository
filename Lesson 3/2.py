#!/usr/bin/python3

point = [0, 0]
print('Начальная позиция:', point)
command = input(
    'Куда будем двигаться?\
        \n1. Влево\
        \n2. Вправо\
        \n3. Вверх\
        \n4. Вниз\
        \n0. Конец движения\
        \n\n')
while (command != "0"): 
    match command:
        case "1":
            point[0] -= 1
            print('Переместились влево:', point)
        case "2":
            point[0] += 1
            print('Переместились вправо:', point)
        case "3":
            point[1] += 1
            print('Переместились наверх:', point)
        case "4":
            point[1] -= 1
            print('Переместились вниз:', point)
        case _:
            print('Введена неверная команда! Попробуй еще раз\n')
    command = input(
    'Куда будем двигаться?\
        \n1. Влево\
        \n2. Вправо\
        \n3. Вверх\
        \n4. Вниз\
        \n0. Конец движения\
        \n\n')
print('\nКонечная позиция:', point)