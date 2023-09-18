'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения
и удаления данных и поиска по фамилии.

'''

from os.path import exists
from csv import DictReader, DictWriter
def get_info():
    info = []
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Not valid number')
            else:
                flag = True
        except ValueError:
            print('Not valid number')
    info.append(phone_number)
    return info

def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()

def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with (open(file_name, encoding='utf-8') as data):
        f_n_reader = DictReader(data)
        phone_book = list(f_n_reader)
    return phone_book

def write_file(list):
    # with open('phone.txt', 'a', encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
    with open('phone.csv', 'w', encoding='utf-8') as data:
        obj = {'Фамилия': list[0], 'Имя': list[1], 'Номер': list[2]}
        res = get_info()
        res.append(obj)
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        for el in res:
            list = f_n_writer.writerow(el)
        return list
    
def record_info(list):
    write_file(list)
    return list

def delete_person(name):
    persons = read_data()
    with open(file_name, 'w', encoding='utf8') as data:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    persons = read_data()
    with open(file_name, "w", encoding="utf8" ) as data:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

def find_contact(info):
    info = get_info()
    result = []
    search = input('Введите элемент для поиска: ')
    for i in info:
        if search in info:
            result = i
            break
        print(read_file(i))
        
def main():
    while True:
        command = input('Выберите одну из команд: W - запись, R - чтение, Q - выход, С - редактирование, D - удаление, F - поиск по фамилии. Введите команду: ')
        create_file()
        if command == 'Q':
            break
        elif command == 'R':
            print(*read_file('phone.csv'))
        elif command == 'W':
            get_info()
            record_info()
            write_file()
        elif command == 'C':
            change_person()
        elif command == 'D':
            delete_contact()
        elif command == 'F':
            find_contact()

main()