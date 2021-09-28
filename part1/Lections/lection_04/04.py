# речь Йоды

prefix = "Я изучаю Python"
postfix = ", мой юный падаван."

new_pr = ' '.join(prefix.split(' ')[::-1])

print(new_pr + postfix)
