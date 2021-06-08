'''
1.Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

# print(argv)
output_in_hours, rate_per_hour, the_prize = argv

try:
    print('Выработка в часах: ', output_in_hours)
    print('Ставка в час: ', rate_per_hour)
    print('Премия: ', the_prize)
    print("Результат выполнения программы: ", (output_in_hours * rate_per_hour) + the_prize)
except ValueError:
    print('Not a number')
