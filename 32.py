"""Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random
n = int(input("Введите число элементов массива: "))
min_d = int(input("Введите минимальное значение диапазона: "))
max_d = int(input("Введите максимальное значение диапазона: "))

list_1 = []
for i in range(n):
    list_1.append(random.randint(0, 100))
print(list_1)

list_ind  = []
for i in range(len(list_1)):
    if list_1[i] >= min_d and list_1[i] <= max_d:
        list_ind.append(i)

print(list_ind)