# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    '''
    Функция принимает 3 аргумента типа int и возвращает сумму наибольших двух
    :param arg_1: int, первое число
    :param arg_2: int, второе число
    :param arg_3: int, третье число
    :return: int, вовращает сумму наибольших двух чисел
    '''
    items_initial = [arg_1, arg_2, arg_3]
    items_initial.remove(min(items_initial))
    return print(sum(items_initial))

my_func(1, 2, 3)