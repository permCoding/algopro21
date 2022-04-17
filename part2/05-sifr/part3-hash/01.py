"""
ввести логин и пароль, сохранить в файле
логин в открытом виде, пароль в виде хэша
"""

login = "junior"
password = "qwerty"

with open("passwords.csv", mode="a", encoding="utf-8") as f:
    f.write(f"{login}|{password}\n")
