string = input()

strFirst = string[:len(string)//2]
strSecond = string[len(string)//2:]


def cryptAll(str1, str2):
    a = 9
    b = 5
    m = 1024
    y0 = 5

    def Gamma(y):
        gamma_list = []
        for i in range(8):
            y = (a * y + b) % m
            gamma_list.append(y)
        return gamma_list

    def encrypt(str):
        gamma = Gamma(y0)
        result_str = ''
        for i in range(len(str)):
            result_str += chr(((ord(str[i]) + gamma[i])))
        return result_str

    def code(str):
        key = '3'
        mas = []
        finalMas = []

        while len(key) != len(str):
            if key[-1] == '3':
                key += '1'
            elif key[-1] == '1':
                key += '4'
            elif key[-1] == '4':
                key += '3'
        for i in range(len(str)):
            sym = ord(str[i]) + int(key[i])
            mas.append(sym)

        for i in range(len(str)):
            finalMas.append(chr(mas[i]))

        return ''.join(finalMas)
    print(encrypt(str1) + code(str2))
    encryptAll(encrypt(str1), code(str2))


def encryptAll(str1, str2):
    a = 9
    b = 5
    m = 1024
    y0 = 5

    def decode(str):
        key = '3'
        mas = []
        finalMas = []

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

    def Gamma(y):
        gamma_list = []
        for i in range(8):
            y = (a * y + b) % m
            gamma_list.append(y)

        return gamma_list

    def decrypt(str):
        gamma = Gamma(y0)
        result_str = ''
        for i in range(len(str)):
            result_str += chr(((ord(str[i]) - gamma[i])))
        return result_str
    print(decrypt(str1) + decode(str2))


cryptAll(strFirst, strSecond)
