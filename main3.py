'''
Поиск всевохможных комбинаций букв и символов латинского языка и кириллицы
Search for all possible combinations of letters and symbols of Latin and Cyrillic
'''

array_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
array_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
array_3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
array_4 = ['/', '&', '$', '%']
array = array_1 + array_2 + array_3 + array_4
variable = ""
last_variable = ""
win = False
combination = 0
last_combination = 0
print("Введите строку, состояющую из этих символов:")
print(array_1)
print(array_2)
print(array_3)
print(array_4)
key = input()
working = True
while working:
    for b in range(len(array)):
        variable = last_variable + array[b]
        combination += 1
        print(f"{variable}     комбинация номер {combination}")
        if variable == key:
            print('Есть совпадение')
            num = 0
            for i in range(len(variable)):
                if variable[i] == array[-1]:
                    num += 1
            if num == len(variable):
                print(f"Последняя комбинация с прошлым количеством символов: {last_combination}")
                print(f"Количество комбинаций с этим количеством символов: {combination - last_combination}")
            working = False
            break

    if working == False: break
    for c in range(len(variable)):
        var = 0
        for char in variable:
            if char == array[-1]:
                var += 1
                if var == len(variable):
                    last_combination = combination
                    for f in range(len(variable)):
                        if f == 0: variable = ""
                        variable += array[0]

                    variable = array[0] + variable
                elif var == len(variable)-1 and variable[0] != array[-1]:
                    for g in range(len(variable)):
                        if g == 0:
                            num = array[array.index(variable[0])+1]
                        else:
                            num += array[0]
                    variable = num


        if variable[-(c+1)] != array[-1]:
            lim = c
            num = ""
            for d in range(len(variable)):
                if d == len(variable) - (lim + 1):
                    num += array[array.index(variable[-(lim+1)])+1]
                else:
                    num += variable[d]
            variable = num
            break

        if variable[-(c + 1)] == array[-1] and c != 0:
            lim = c
            num = ""
            for d in range(len(variable)):
                if d == len(variable) - (lim + 1):
                    num += array[0]
                else:
                    num += variable[d]
            variable = num


    last_variable = ""
    for e in range(len(variable)-1):
        last_variable += variable[e]