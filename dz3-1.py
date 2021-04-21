def my_func(ch_1, ch_2):
    if ch_2 == 0:  # исключает деление на ноль
        print('Введено неверное значение ch_2')
    else:
        div = ch_1 / ch_2
        print(round(div, 4))


my_func(float(input('ch_1: ')), float(input('ch_2: ')))
