'''
2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def contact_data(name, surname, year_of_birth, city_of_residence, email, phone):
    return (
        f'Имя - {name}, Фамилия - {surname}, Год рождения - {year_of_birth}, Город проживания - {city_of_residence} '
        f' email - {email}, телефон - {phone}')


print(contact_data(name="Владимир", surname="Цуба", year_of_birth='2001', city_of_residence="Лепель",
                   email="vladimiralfa@inbox.ru", phone="+375292956845"))
