file = open("numbers.txt")
text = file.read()
file.close()

# print(text)
# print(text.split("\n"))
for line in text.split("\n"):
    print(line)
