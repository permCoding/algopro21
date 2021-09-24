def play(maxCount=3, xLeft=10, xRight=99):
    count = 1
    while True:
        x = int(input(f"Попытка {count}. Введите число [{xLeft},{xRight}] - "))
        if count >= maxCount or xLeft <= x <= xRight:
            break
        count += 1
    return -1 if count > maxCount else x


maxCount, xLeft, xRight = 3, 10, 99
num = play()
if num < 0:
    print("Повтор попыток через 60 сек.")
else:
    print(num)
