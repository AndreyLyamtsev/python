month = int(input("Введите месяц: "))
day = int(input("Введите день: "))
if month == 1 and 1 <= day <= 20:
    print("Ваш знак зодиака Козерог")
elif month == 12 and 23 <= day < 31:
    print("Ваш знак зодиака Козерог")
elif month == 1 and 21 <= day <= 31:
    print("Ваш знак зодиака Водолей")
elif month == 2 and 1 <= day <= 19:
    print("Ваш знак зодиака: Водолей")
elif month == 2 and 1 <= day <= 20:
    print("Ваш знак зодиака: Рыбы")
elif month == 3 and 1 <= day <= 20:
    print("Ваш знак зодиака: Рыбы")
elif month == 3 and 21 <= day <= 31:
    print("Ваш знак зодиака: Овен")
elif month == 4 and 1 <= day <= 20:
    print("Ваш знак зодиака: Овен")
elif month == 4 and 21 <= day <= 30:
    print("Ваш знак зодиака: Телец")
elif month == 5 and 1 <= day <= 21:
    print("Ваш знак зодиака: Телец")
elif month == 5 and 22 <= day <= 31:
    print("Ваш знак зодиака: Близнецы")
elif month == 6 and 1 <= day <= 21:
    print("Ваш знак зодиака: Близнецы")
elif month == 6 and 22 <= day <= 30:
    print("Ваш знак зодиака: Рак")
elif month == 7 and 1 <= day <= 22:
    print("Ваш знак зодиака: Рак")
elif month == 7 and 23 <= day <= 31:
    print("Ваш знак зодиака: Лев")
elif month == 8 and 1 <= day <= 23:
    print("Ваш знак зодиака: Лев")
elif month == 8 and 24 <= day <= 31:
    print("Ваш знак зодиака: Дева")
elif month == 9 and 1 <= day <= 23:
    print("Ваш знак зодиака: Дева")
elif month == 9 and 24 <= day <= 30:
    print("Ваш знак зодиака: Весы")
elif month == 10 and 1 <= day <= 23:
    print("Ваш знак зодиака: Весы")
elif month == 10 and 24 <= day <= 31:
    print("Ваш знак зодиака: Скорпион")
elif month == 11 and 1 <= day <= 22:
    print("Ваш знак зодиака: Скорпион")
elif month == 11 and 23 <= day <= 30:
    print("Ваш знак зодиака: Стрелец")
elif month == 12 and 1 <= day <= 22:
    print("Ваш знак зодиака: Стрелец")
else:
    print("Введены некорректные данные")
