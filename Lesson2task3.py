'''
3.
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
variable_1 = int(input("Введите реализацию:\n 1:List \n 2:Dict\n"))
counter = 0
if variable_1 == 1:
    my_list = ['Январь', "Февраль", "Март", "Апрель", "Май", "Июнь",
               "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    answer_user = int(input("Введите месяц: "))
    for bmv in my_list:
        counter += 1
        if answer_user == counter:
            print("Ваш месяц: ", bmv)
            if counter == 1 or counter == 2 or counter == 12:
                print("Это месяц относится к зиме")
            elif counter == 3 or counter == 4 or counter == 5:
                print("Это месяц относится к весне")
            elif counter == 6 or counter == 7 or counter == 8:
                print("Это месяц относится к лету")
            else:
                print("Это месяц относится к осени")
else:
    my_dict = {1: 'Январь', 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
               7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    answer_user = int(input("Введите меяц: "))
    print("Ваш месяц: ", my_dict[answer_user])
    for bmv in my_dict:
        counter += 1
        if answer_user == counter:
            if counter == 1 or counter == 2 or counter == 12:
                print("Это месяц относится к зиме")
            elif counter == 3 or counter == 4 or counter == 5:
                print("Это месяц относится к весне")
            elif counter == 6 or counter == 7 or counter == 8:
                print("Это месяц относится к лету")
            else:
                print("Это месяц относится к осени")
