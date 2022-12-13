#!/usr/bin/python3

inventory = dict()
maxweight = float(input('Введите размер инвентаря: '))
weight = 0.0
command = input('Что хотите сделать?\n1. добавить предмет в инвентарь\n2. удалить предмет из инвентаря\n3. узнать вес инвентаря\n4. вывести содержимое инвентаря\n')
while(command != '4'):
    match command:
        case '1':
            item = input('\nВведите предмет: ')
            item_weight = float(input('Введите вес предмета: '))
            if (weight+item_weight <= maxweight):
                inventory[item] = item_weight
                weight += item_weight
            else:
                print('Размер предмета превышает вес инвентаря! Добавить предмет невозможно')
        case '2':
            delete = input('Введите название предмета, который хотите удалить: ')
            if (delete not in inventory):
                print('Такого предмета в инвентаре нет')
            else:
                weight -= inventory[delete]
                inventory.pop(delete, print('Предмет успешно удален'))
        case '3':
            print('Общий вес:', weight)
            print('Максимальный вес:', maxweight)
        case _:
            print('Введена неверная команда! Попробуй еще раз')
    command = input('\nЧто хотите сделать?\n1. добавить предмет в инвентарь\n2. удалить предмет из инвентаря\n3. узнать вес инвентаря\n4. вывести содержимое инвентаря\n')
print('Содержимое инвентаря, сортированное по весу:')
sorted_inventory = dict(sorted(inventory.items(), key=lambda item: item[1]))
for i, w in sorted_inventory.items():
    print(i, ':', w)

