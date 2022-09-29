import json

with open('users.json') as f:
    data = json.load(f)

for persone in data:
    if persone['age'] >= 25:
        print(json.dumps(persone, indent=2))

