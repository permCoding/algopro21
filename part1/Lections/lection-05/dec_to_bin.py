dec = int(input("Введите десятичное число - "))
bin = ""
while dec > 0:
    ost = dec % 2
    dec = dec // 2
    bin = str(ost) + bin
print(bin)
