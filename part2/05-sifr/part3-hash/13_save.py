import json


user_1 = {"login": "Aelita", "password": "mars"}

login, password = "Ilon", "mask"
user_2 = {}
user_2["login"] = login
user_2["password"] = password

users = [user_1, user_2]  # list

with open('users_save.json', 'w') as f:
    json.dump(users, f, indent=4)
