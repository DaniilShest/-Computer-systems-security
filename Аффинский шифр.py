from operator import index, mod

a = 2
b = 5

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
strHead = input('Введите сообщение: ')


def encrypt(str):
    newStr = ''
    for i in range(len(str)):
        num = abc.index(str[i])
        cryptNum = mod((a * num + b), 33)
        newStr = newStr + abc[cryptNum]
    return newStr


def decrypt(str):
    newStr = ''
    ind = 1
    findA = True
    while findA:
        if ind % a == 0 and ind % 33 == 1:
            break
        ind += 1
    for i in range(len(str)):
        num = abc.index(str[i])
        cryptNum = int(mod((ind / a) * (num - b), 33))
        newStr += abc[cryptNum]
    return newStr


encryptStr = encrypt(strHead)
decryptStr = decrypt(encryptStr)

print(encryptStr)
print(decryptStr)
