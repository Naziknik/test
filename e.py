import json

with open('users.json') as f:
    data = json.load(f)

largest_number = data[0]['friends'][0]['age']

for persone in data:
    for friend in persone['friends']:
        if friend['age'] > largest_number:
            largest_number = friend['age']       
            print(json.dumps(persone, indent=2))

