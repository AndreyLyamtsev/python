def my_func():
    s = 0
    while True:
        line = input()
        l1 = line.split()
        for el in l1:
            if el == '*':
                return s
            else:
                s = s + int(el)
        print(s)


my_func()
