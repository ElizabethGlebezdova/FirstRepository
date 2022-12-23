def xor_encode(string, key):
    result = ''
    for i in range(len(string)):
        result += chr(ord(string[i]) ^ ord(key[i % len(key)]))
    return result

def xor_decode(byteline, key):
    result = bytearray()
    for i in range(len(byteline)):
        result.append(byteline[i] ^ key[i % (len(key))])
    return result

print("XOR-шифрование")
try:
    with open('Lesson 6\input-xor.txt', "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Файл не найден!")
else:
    encode_text = xor_encode(text, input('Введите ключ-слово: '))
    print('Результат шифрования:', encode_text)
    with open('output-xor.txt', "w") as f:
        f.write(encode_text)

print("XOR-дешифрование")
try:
    with open('Lesson 6\output-xor.txt', "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Файл не найден!")
else:
    decode_text = xor_encode(text, input('Введите ключ-слово: '))
    print('Результат дешифрования:', decode_text)