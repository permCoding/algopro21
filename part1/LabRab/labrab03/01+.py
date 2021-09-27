def play(maxCount=3, xLeft=10, xRight=99):
    count, x = 1, 0
    while True:
        x = int(input(f"Попытка {count}. Введите число [{xLeft},{xRight}] - "))
        count += 1
        checkCount = count <= maxCount
        checkNumber = xLeft <= x <= xRight
        if checkNumber or not checkCount:
            break
        
    return (checkNumber, x)


maxCount, xLeft, xRight = 3, 10, 99
check, num = play()
if check:
    print("Выбрано число -", num)
else:
    print("Повтор попыток через 60 сек.")
