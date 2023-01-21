# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

'''
Задача без использования list comprehension:

Реализуйте алгоритм перемешивания списка.
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум
использование библиотеки Random для и получения случайного int

import random

my_list = []

for x in range(5):
    my_list.append(random.randint(1,8))

print (f"Начальный список: " + str(my_list))
for i in range(len(my_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]

print ("Перемешанный список: " +  str(my_list))

'''


#Улучшение кода с использованием list comprehension
import random
from random import randint as RI

my_list = []

my_list = [RI(0, 8) for x in range(5)]#list comprehension

print(f"Начальный список: " + str(my_list))
for i in range(len(my_list) - 1, 0, -1):
    j = random.randint(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]


print("Перемешанный список: " + str(my_list))


