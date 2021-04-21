def my_func(x, y):
    if x <= 0 or y >= 0:
        return print('Введены неверные аргументы')
    else:
        st = x ** y
        print(round(st, 4))


my_func(float(input('Введите значение аргумента x: ')), int(input('Введите значение аргумента y: ')))
print(31 * '=')  # разделение 1-го и 2-го способов


def my_f(x, y):
    if x <= 0 or y >= 0:
        return print('Введены неверные аргументы')
    else:
        r = 1
        while y < 0:
            r /= x
            y = y + 1
    print(round(r, 4))


my_f(float(input('Введите значение аргумента x: ')), int(input('Введите значение аргумента y: ')))