#!/usr/bin/python3

def check_passwd(password):
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

password = input('Введите пароль: ')
if (check_passwd(password)):
    print('Ваш пароль корректен!')
else:
    print('Ваш пароль не корректен!')