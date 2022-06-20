'''
Шифратор и дешифратор методом перестановки в одном файле
Encoder and decoder by permutation method in one file
'''


def Encryption(message, key):
    array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    array_3 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    array_4 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    array_5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    array_6 = ['/', '&', '$', '%', '?', '!', ',', '.', '@', ':', ';', '*', '+', '=', '-', '_', '\'', '\"', '|', '^', '`', '~', '(', ')', '{', '}', '[', ']']
    array = array_1 + array_2 + array_3 + array_4 + array_5 + array_6
    try:
        num = 0
        step_new = ""
        for char in str(key):
            if char not in array_5 and (char in array_1 or char in array_2):
                num += (array_1 + array_2).index(char)
            else:
                step_new += str(char)
        if step_new == "":
            key_new = num
        else:
            key_new = int(step_new) + num
    except:
        print("Криптографический ключ должен состоять только из букв латинского алфавита и цифр. Повторите пожалуйста.")

    message_new = ""
    for i in range(len(message)):
        if message[i] in array:
            message_new += array[(array.index(message[i]) + key_new) % len(array)]
        else:
            message_new += message[i]
    return message_new

def Decryption(message, key):
    array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    array_3 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    array_4 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    array_5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    array_6 = ['/', '&', '$', '%', '?', '!', ',', '.', '@', ':', ';', '*', '+', '=', '-', '_', '\'', '\"', '|', '^', '`', '~', '(', ')', '{', '}', '[', ']']
    array = array_1 + array_2 + array_3 + array_4 + array_5 + array_6
    try:
        num = 0
        step_new = ""
        for char in str(key):
            if char not in array_5 and (char in array_1 or char in array_2):
                num += (array_1 + array_2).index(char)
            else:
                step_new += str(char)
        if step_new == "":
            key_new = num
        else:
            key_new = int(step_new) + num
    except:
        print("Криптографический ключ должен состоять только из букв латинского алфавита и цифр. Повторите пожалуйста.")

    message_new = ""
    for i in range(len(message)):
        if message[i] in array:
            message_new += array[(array.index(message[i]) - key_new) % len(array)]
        else:
            message_new += message[i]
    return message_new



