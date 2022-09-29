import json

with open('users.json') as f:
    data = json.load(f)

for persone in data:
    if persone['gender'] == 'female' and persone['isActive'] == True:
        print(json.dumps(persone, indent=2))

