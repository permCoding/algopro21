import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex  # для генерации случайного сдвига
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def get_users(file_name):
    with open(file_name, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        res = map(lambda line: (line.split('|')[0], line.split('|')[1].strip()), lines)
    return list(res)


users = get_users("users.csv")
print(users)  # это просто для контроля

print('Диалог доступа к приватным данным')
login = input('Введите login: ')

user = list(filter(lambda user: user[0] == login, users))
if not user:
    print("нет такого пользователя")
else:
    login, hash_pass = user[0][0], user[0][1]
    password = input('Введите password: ')
    if check_password(hash_pass, password):
        print('Пароли совпадают\nдоступ к БД получен')
    else:
        print('Пароли не совпадают\nнет доступа к БД')
