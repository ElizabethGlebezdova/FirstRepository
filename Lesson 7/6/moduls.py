def check_passwd(password):
    """Проверка пароля

    Принимает:
        password = строка пароля
    Возвращает:
        true - пароль корректный
        false - пароль некорректный
    """
    check = True
    if (len(password) < 6):
        print('Пароль должен быть не менее 6 символов!')
        check = False
    if not any(ch.isdigit() for ch in password):
        print('Пароль должен содержать хотя бы одну цифру!')
        check = False
    if not any(ch.isalpha() for ch in password):
        print('Пароль не должен состоять только из цифр!')
        check = False
    if ('password' in password.lower()):
        print('Пароль не должен содержать слово "password"!')
        check = False
    return check

def strings_to_bytecodes(list):
    """Перевод списка строк в список байт кодов"""
    byteCodes = []
    for i in list:
        byteCodes.append(i.encode('utf-8'))
    return byteCodes

def bytecodes_to_strings(list):
    """Перевод списка байт кодов в список строк"""
    strings = []
    for i in list:
        strings.append(i.decode('utf-8'))
    return strings

def fibonacci(n):
    """Нахождение значения заданного номера числа Фибоначчи
    
    Принимает:
        n - номер числа Фибоначчи
    Возвращает:
        Значение номера Фибоначчи
    """
    if (n == 0):
        return 0
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)