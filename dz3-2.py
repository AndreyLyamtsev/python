def my_func(name, surname, year_of_birth, city, email, ph_number):
    print(name, surname, year_of_birth, city, email, ph_number, sep=',')


my_func(name=input('Введите имя: '), surname=input('Введите фамилию: '), year_of_birth=input('Введите год рождения: '),
        city=input('Введите город проживания: '), email=input('Введите email: '),
        ph_number=input('Введите номер телефона: '))
