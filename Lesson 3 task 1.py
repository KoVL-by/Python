'''
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def division_function(s_1, s_2):
    try:
        s_1/s_2
    except ZeroDivisionError:
        print("Результат: ")
        return 0
    else:
        print("Результат деления :")
        return s_1 / s_2


print(division_function(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
