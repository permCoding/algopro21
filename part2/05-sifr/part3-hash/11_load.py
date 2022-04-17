import json

with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)
    for user in users:
        print(user)
