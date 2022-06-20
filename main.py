'''
Строка из 65 рандомных сиволов
A string of 65 random characters
'''
import random

start = True
variable = ""
array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'z']
array_3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
array_4 = ['/', '&', '$', '%']
array = array_1 + array_2 + array_3 + array_4
while start:
    variable = ""
    for i in range(150):
        variable += array[random.randint(0, 65)]
    print(variable)
