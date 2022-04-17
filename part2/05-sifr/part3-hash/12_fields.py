import json

with open('users.json', 'r', encoding='utf-8') as f:
    print('login'.ljust(12, ' '), 'password')
    users = json.load(f)
    for user in users:
        print(user["login"].ljust(12, ' '), user["password"])
