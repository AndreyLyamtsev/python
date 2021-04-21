def my_func(word):
    word = word.title()  # переводит 1-ую букву слова в верхний регистр
    print(word)
    print(20 * '*')


my_func(input('Введите слово: '))
some_words = input('Введите слова, разделенные пробелом: ')
my_func(some_words)
