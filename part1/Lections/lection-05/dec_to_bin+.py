# def decToBin():  # camel case
def dec_to_bin(dec):  # snake case
    bin = ""
    while dec > 0:
        ost = dec % 2
        dec = dec // 2
        bin = str(ost) + bin
    return bin


dec = int(input("Введите десятичное число - "))
print(dec_to_bin(dec))
