# Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании
# \ студентами вуза \ учениками школы

import data_base as db
import salary as sal


def option():
    ch = int(input('Введите предмет поиска в данных работника: \n \
    1: Персональные данные \n \
    2: Оклад \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Su = str(input("Введите фамилию работника: "))
        if Su in db.data_personal['Фамилия']:
            index = db.data_personal['Фамилия'].index(Su)
        print(
            f"{db.data_personal['ID'][index]}, {db.data_personal['Имя'][index]},{db.data_personal['Фамилия'][index]}\n,{db.data_personal['Дата рождения'][index]}, {db.data_personal['Должность'][index]}")
        print('\nХотите выполнить другую операцию? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Для получения информации об окладе введите ID работника: ')
        if c in sal.salary['ID']:
            index = sal.salary['ID'].index(c)
            print(f" Оклад = {sal.salary['Оклад'][index]}")
            print('\nХотите выполнить другую операцию? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()
