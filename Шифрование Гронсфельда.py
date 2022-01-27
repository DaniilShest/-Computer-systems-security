str = input('Введите сообщение: ')
def code(str):
    key = '3'
    mas = [];
    finalMas = [];

    while len(key) != len(str):
        if key[-1] == '3':
            key += '1'
        elif key[-1] == '1':
            key += '4'
        elif key[-1] == '4':
            key += '3'    
    print('Ключ: ' + key)
    for i in range(len(str)):
        sym = ord(str[i]) + int(key[i])
        mas.append(sym)
    
    for i in range(len(str)):
        finalMas.append(chr(mas[i]))

    return ''.join(finalMas)

def decode(str):
    key = '3'
    mas = [];
    finalMas = [];

    while len(key) != len(str):
        if key[-1] == '3':
            key += '1'
        elif key[-1] == '1':
            key += '4'
        elif key[-1] == '4':
            key += '3'

    for i in range(len(str)):
        sym = ord(str[i]) - int(key[i])
        mas.append(sym)
    
    for i in range(len(str)):
        finalMas.append(chr(mas[i]))

    return ''.join(finalMas)

cStr = code(str)
dStr = decode(cStr)
print('Зашифрованно: ' + cStr)
print('Рашифрованно: ' + dStr)
