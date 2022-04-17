import json

line_json = '{"login": "Aelita", "password": "mars"}'

user = json.loads(line_json)

print(user)  # dict = keys + values

print(user["login"], user["password"])
