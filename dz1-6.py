a = int(input())
b = int(input())
day = 1
distance = a
while True:
    day = day + 1
    distance = distance + a * 10 / 100
    print(day,"-й день", f"{distance:.1f}", "км")
    if distance >= b:
        break
    if distance < b:
        continue

