def play(maxCount=3, xLeft=10, xRight=99):
    count = 1
    x = int(input(f"Попытка {count}. Введите число [{xLeft},{xRight}] - "))
    while (count < maxCount) and (x < xLeft or x > xRight):
        count += 1
        x = int(input(f"Попытка {count}. Введите число [{xLeft},{xRight}] - "))
    return -1 if count >= maxCount else x


maxCount, xLeft, xRight = 3, 10, 99
num = play()
if num < 0:
    print("Повтор попыток через 60 сек.")
else:
    print(num)
