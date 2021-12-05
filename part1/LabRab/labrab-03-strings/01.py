def play(maxCount=3, xLeft=10, xRight=99):
    count, x = 1, 0
    while True:
        x = int(input(f"Попытка {count}. Введите число [{xLeft},{xRight}] - "))
        if count >= maxCount or xLeft <= x <= xRight:
            break
        count += 1
    return (count < maxCount, x)


maxCount, xLeft, xRight = 3, 10, 99
check, num = play()
if check:
    print(num)
else:
    print("Повтор попыток через 60 сек.")
