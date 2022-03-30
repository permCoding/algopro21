# рекурсия

def func1():
    global x
    x += 5
    print(x)


def func2():
    global lst
    lst += [3,55]
    print(lst)


# x = 55
# func1()
# print(x)

lst = [1,2,3,4]
func2()
print(lst)
