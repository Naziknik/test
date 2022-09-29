import json

with open('users.json') as f:
    data = json.load(f)

largest_number = data[0]['balance']

for persone in data:
    if persone['balance'] > largest_number:
        largest_number = persone['balance']       

print(largest_number)

