import uuid
import hashlib
from os.path import exists


class User:
    def __int__(self, line):
        args = line.split('|')
        self.login = args[0]
        self.password = args[1].strip()


def hash_password(password):
    salt = uuid.uuid4().hex  # для генерации случайного сдвига
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def get_users(file_name):
    if exists(file_name):
        with open(file_name, mode="r", encoding="utf-8") as f:
            return list(map(lambda line: User(line), f.readlines()))
    return []


users = get_users("users.csv")
print(users)  # это просто для контроля

print('Регистрация нового пользователя')
login = input('Введите login: ')

user = list(filter(lambda user: user.login == login, users))
if user:
    print("Этот login уже занят")
else:
    password = input('Введите password: ')
    hash_pass = hash_password(password)
    print(hash_pass)  # это для контроля

    with open("users.csv", mode="a", encoding="utf-8") as f:
        f.write(f"{login}|{hash_pass}\n")
