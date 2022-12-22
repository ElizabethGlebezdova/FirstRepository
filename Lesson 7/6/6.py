import moduls as md

print('Подходит ли пароль 1234hello:', md.check_passwd('1234hello'))
list_str = ['123', 'hello', 'привет!']
print('Перевод списка строк в список байт кодов:', md.strings_to_bytecodes(list_str))
list_bytecodes = [b'567', b'world', b'\xd0\xbc\xd0\xb8\xd1\x80']
print('Перевод списка байт кодов в список строк:', md.bytecodes_to_strings(list_bytecodes))
print('29 число Фибоначчи равно', md.fibonacci(29))