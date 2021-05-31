'''
2.Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
my_list = []
user_list = input("Введите элемет списка:")
my_list.append(user_list)
while True:
    user_response = input("Добавить ещё один элемент списка?\n 1:Да\n 2:Нет\n 3:Просмотреть список\n")
    if user_response == "1":
        user_list = input("Введите элемет списка:")
        my_list.append(user_list)
    elif user_response == '2':
        print('Отлично,продолжим :)')
        break
    elif user_response == '3':
        print("Ваш список: ", my_list)
i = 0
my_list_1 = []
repository = ""
index = ''
for index in my_list:
    i += 1
    if i % 2 != 0:
        repository = index
    elif i % 2 == 0:
        my_list_1.append(index)
        my_list_1.append(repository)
my_list_1.append(index)
my_list = my_list_1
print("Результат программы: ", my_list)
