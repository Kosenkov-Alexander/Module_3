# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_div(user_number_1, user_number_2):
    while True:
        user_number_1 = int(input('Введите число: '))
        user_number_2 = int(input('Введите число: '))
        if user_number_2 == 0:
            print('Вы пытаетесь поделить на ноль')
            continue
        else:
            break
    result = user_number_1 / user_number_2
    return result

print(func_div(10, 5))