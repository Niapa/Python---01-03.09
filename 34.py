"""Задача 34:  Винни-Пух попросил Вас посмотреть,
есть ли в его стихах ритм. Поскольку разобраться
в его кричалках не настолько просто, насколько легко
он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения
одинаковое. Фраза может состоять из одного слова,
если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам

1 вар.:
poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
phrase = poem.split()

lst = [sum(x in 'аеёиоуыэюя' for x in el) for el in phrase]

if len(set(lst)) == 1:
    res = "Парам пам-пам"
else:
    res = "Пам парам"

print(res)
"""


def phrase():

    poem = input("Введите стих: ").lower().split()
    count = lambda x: sum(1 for i in x if i in "аеёиоуыэюя")
    temp = count(poem[0])

    if all(count(i) == temp for i in poem):
        print("Парам пам-пам")
    else:
        print("Пам парам")

phrase()