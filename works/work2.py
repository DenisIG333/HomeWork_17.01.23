# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


'''
Задача без использования map:

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


compr_text = input("Введите данные: ")
temp = compr_text[:] + " "
array = []


def packing():
    global temp
    count = 1
    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            count += 1
        else:
            array.append(str(count) + temp[i])
            count = 1
    print("".join(array))
    temp = "".join(array)


def unpack():
    global temp
    for i in range(len(compr_text) - 1):
        if compr_text[i].isdigit():
            elem = int(compr_text[i]) * compr_text[i + 1]
            change = compr_text[i] + compr_text[i + 1]
            temp = temp.replace(change, elem)
    print(temp)



def check_input():
    check = False
    count = 0
    for item in range(len(compr_text)):
        if compr_text[item].isdigit():
            count += 1
            print(check)
    if count > 0:
        check = True
    else:
        check = False

    if check == True:
        unpack()
    if check == False:
        packing()


def user_input_data():
    with open('input_data.txt', 'w') as data:
        data.write(compr_text)
    data.close()


def user_output_data():
    global temp
    with open('output_data.txt', 'w') as data:
        data.write(temp)
    data.close()


check_input()
user_input_data()
user_output_data()
'''

#Улучшение кода с использованием map

compr_text = input("Введите данные: ")
temp = compr_text[:] + " "
array = []


def packing():
    global temp
    count = 1
    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            count += 1
        else:
            array.append(str(count) + temp[i])
            count = 1
    print("".join(array))
    temp = "".join(array)


def unpack():
    global temp
    for i in range(len(compr_text) - 1):
        if compr_text[i].isdigit():
            elem = int(compr_text[i]) * compr_text[i + 1]
            change = compr_text[i] + compr_text[i + 1]
            temp = temp.replace(change, elem)
    print(temp)



def check_input(): #здесь используется map
    check = any(map(str.isdigit, compr_text))
    if check == True:
        unpack()
    if check == False:
        packing()


def user_input_data():
    with open('input_data.txt', 'w') as data:
        data.write(compr_text)
    data.close()


def user_output_data():
    global temp
    with open('output_data.txt', 'w') as data:
        data.write(temp)
    data.close()


check_input()
user_input_data()
user_output_data()

