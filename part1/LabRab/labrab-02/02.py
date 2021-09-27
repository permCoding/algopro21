def get_count_div(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count

n = 12
print(get_count_div(n))
