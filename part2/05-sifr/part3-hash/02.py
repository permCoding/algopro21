import hashlib  # стандартная библиотека


def get_hash_md5(line):  # перевести в байты и закодировать
    hash_object = hashlib.md5(line.encode())
    return hash_object.hexdigest()


def get_hash_sha1(line):  # перевести в байты и закодировать
    hash_object = hashlib.sha1(line.encode())
    return hash_object.hexdigest()


def get_hash_sha256(line):  # перевести в байты и закодировать
    hash_object = hashlib.sha256(line.encode())
    return hash_object.hexdigest()


print(hashlib.algorithms_guaranteed)  # алгоритмы модуля

password = "qwerty"

hash_md5 = get_hash_md5(password)
print(hash_md5)
print(len(hash_md5))

hash_sha1 = get_hash_sha1(password)
print(hash_sha1)
print(len(hash_sha1))


hash_sha256 = get_hash_sha1(password)
print(hash_sha256)
print(len(hash_sha256))


# with open("passwords.csv", mode="a", encoding="utf-8") as f:
#     f.write(f"{login}|{password}\n")
