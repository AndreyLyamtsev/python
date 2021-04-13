n = int(input())
max1 = 0
while n > 0:
    lost = n % 10  # отделяем последнюю цифру
    if lost > max1:
        max1 = lost
    n = n // 10  # уменьшаем число на одну цифру
lost1 = n % 10  # отделяем последнюю
print(max1)
