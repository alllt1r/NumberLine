'''
Простой дешифратор методом перестановки
A simple decoder by the permutation method
'''


array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
array_3 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
array_4 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
array_5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
array_6 = ['/', '&', '$', '%', '?', '!', ',', '.', '@', ':', ';', '*', '+', '=', '-', '_', '\'', '\"', '|', '^', '`', '~', '(', ')', '{', '}', '[', ']']
array = array_1 + array_2 + array_3 + array_4 + array_5 + array_6
array = array_2

'''
message = input("Введите строчку для дешифровки ")
message_new = ""
for b in range(len(array)):
    message_new = ""
    for i in range(len(message)):
        if message[i] in array:
            message_new += array[(array.index(message[i]) + b) % len(array)]
        else:
            message_new += message[i]

    print(f"Результат 1: {message_new}")
    message_new2 = ""
    for c in range(len(message_new)):
        if message[c] in array:
            message_new2 += array[-(array.index(message_new[c])+1)]
        else:
            message_new2 += message[c]
    print(f"Результат 2: {message_new2}")
    print("")
'''




message = input("Введите строчку для дешифровки ")
message_new = ""
for b in range(len(array)):
    message_new = ""
    for i in range(len(message)):
        if message[i] in array:
            message_new += array[(array.index(message[i]) + b) % len(array)]
        else:
            message_new += message[i]

    print(f"Результат: {message_new}")


'''
message = input("Введите строчку для дешифровки ")
message_new = ""
crypt = 0
key = "ЛОХЩЩ"
for i in range(len(message)):

    if message[i].upper() in array:
        if message[i].islower():
            message_new += array[(array.index(message[i].upper()) - array.index(list(key)[crypt])) % len(array)].lower()
        else:
            message_new += array[(array.index(message[i].upper()) - array.index(list(key)[crypt])) % len(array)].upper()
        if crypt >= 4:
            crypt = 0
        else:
            crypt += 1
    else:
        message_new += message[i]

print(f"Результат: {message_new}")
'''




'''
message = input("Введите строчку для дешифровки ")
message_new = ""
for b in range(len(array)):
    message_new = ""
    for i in range(len(message)):
        if message[i] in array:
            message_new += array[(array.index(message[i]) - b) % len(array)]
        else:
            message_new += message[i]

    print(f"Результат: {message_new}")
'''


'''


array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
array_3 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
array_4 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
array_5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
array_6 = ['/', '&', '$', '%', '?', '!', ',', '.', '@', ':', ';', '*', '+', '=', '-', '_', '\'', '\"', '|', '^', '`', '~', '(', ')', '{', '}', '[', ']']
array = array_1 + array_2 + array_3 + array_4 + array_5 + array_6
array = array_2


check = True
while check:
    try:
        step = input("Введите криптографический ключ шифрования для дешифровки ")
        num = 0
        step_new = ""
        for char in str(step):
            if char not in array_5 and (char in array_1 or char in array_2):
                num += (array_1 + array_2).index(char)
            else:
                step_new += str(char)
        if step_new == "":
            step = num
        else:
            step = int(step_new) + num
        check = False
    except:
        print("Ключ должен состоять только из букв латинского алфавита и цифр. Повторите пожалуйста.")

message = input("Введите строчку для дешифровки ")
message_new = ""
for i in range(len(message)):
    if message[i] in array:
        message_new += array[(array.index(message[i]) - step) % len(array)]
    else:
        message_new += message[i]

print(f"Результат: {message_new}")
'''
