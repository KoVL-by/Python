'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
number = counter = int(input("Введите любое целое число: "))
maximum = int(0)
while True:
    number %= 10
    if maximum < number:
        maximum = number
    counter = int((counter-number)/10)
    number = counter
    if counter == 0:
        print("Самое большое число: ", maximum)
        break
