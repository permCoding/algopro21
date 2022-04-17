'''сдвиг и дополнительные символы позволят уменьшить
вероятность совпадения кэшей от разных входных строк'''
import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex  # для генерации случайного сдвига
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)

print('Строка для хранения в базе данных: ' + hashed_password)
check_pass = input('Введите пароль еще раз для проверки: ')

if check_password(hashed_password, check_pass):
    print('Пароли совпадают - сохраняем в БД')
else:
    print('Пароли не совпадают...')
