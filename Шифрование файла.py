from random import randint

task = int(input('Что хотите сделать с файлом:\n1.Зашифровать\n2.Расшифровать\n'))

if task == 1:
    firstFile = input('Введите название файла: ')
    fileText = open(firstFile).read()
    key = randint(100, 1000)

    def code(fileText, key):
        mas = []
        finalMas = []
        key = str(key)
        finalKey = ''

        while len(finalKey) < len(fileText):
            finalKey += key

        for i in range(len(fileText)):
            sym = ord(fileText[i]) + int(finalKey[i])
            mas.append(sym)

        for i in range(len(fileText)):
            finalMas.append(chr(mas[i]))

        print(''.join(finalMas))
        return ''.join(finalMas)

    finalFile = open('encrypt.txt', 'w+')
    b = "Зашифрованное сообщение:"
    finalFile.write(f"Ключ: {key}\n{b}\n{code(fileText, key)}")
    print('Файл успешно зашифрован')

elif task == 2:
    try:
        firstFile = input('Введите название файла: ')
        key = input('Введите ключ: ')
        lines = open(firstFile).readlines()[2:]
        lines = lines[0]

        def decode(str, key):
            mas = []
            finalMas = []

            finalKey = ''

            while len(finalKey) < len(str):
                finalKey += key

            for i in range(len(str)):
                print(i)
                sym = ord(str[i]) - int(finalKey[i])
                mas.append(sym)

            for i in range(len(str)):
                finalMas.append(chr(mas[i]))

            return ''.join(finalMas)

        finalFile = open('decryptFile.txt', 'w+')
        finalFile.write(f"Расшифрованное сообщение: {decode(lines, key)}")
        print('Файл успешно расшифрован')
    except:
        print('Ошибка')
else:
    print('Такой опции не существует')
