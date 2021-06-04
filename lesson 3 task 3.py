'''
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


def my_func(var_1, var_2, var_3):
    print(f'Ваши аргументы:\n1-ый: {var_1}\n2-ой: {var_2}\n3-ий: {var_3}')
    my_list = [var_1, var_2, var_3]
    my_list.remove(min(my_list))
    sum_1 = sum(my_list)
    print('Сумма наибольших двух аргументов: ')
    return sum_1


print(my_func(1, 2, 3))
