import hashlib  # стандартная библиотека


def get_hash_sha1(line):  # перевести в байты и закодировать
    hash_object = hashlib.sha1(line.encode())
    return hash_object.hexdigest()


print(hashlib.algorithms_guaranteed)  # алгоритмы модуля

login = "jun"
password = "qwe"

hash_sha1 = get_hash_sha1(password)
print(hash_sha1)

with open("users.csv", mode="a", encoding="utf-8") as f:
    f.write(f"{login}|{hash_sha1}\n")
