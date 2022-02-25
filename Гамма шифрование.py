a = 9
b = 5
m = 4096
y0 = 502
string = input()
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


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


def decrypt(str):
    gamma = Gamma(y0)
    result_str = ''
    for i in range(len(str)):
        result_str += chr(((ord(str[i]) - gamma[i])))
    return result_str


print(encrypt(string))
print(decrypt(encrypt(string)))
