import uuid
import hashlib
from os.path import exists


def hash_password(password):
    salt = uuid.uuid4().hex  # для генерации случайного сдвига
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def get_users(file_name):
    if exists(file_name):
        with open(file_name, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            mp = map(lambda line: (line.split('|')[0], line.split('|')[1].strip()), lines)
            return list(mp)
    return []


users = get_users("users.csv")
print(users)  # это просто для контроля

print('Регистрация нового пользователя')
login = input('Введите login: ')

user = list(filter(lambda user: user[0] == login, users))
if user:
    print("Этот login уже занят")
else:
    password = input('Введите password: ')
    hash_pass = hash_password(password)
    print(hash_pass)

    with open("users.csv", mode="a", encoding="utf-8") as f:
        f.write(f"{login}|{hash_pass}\n")
