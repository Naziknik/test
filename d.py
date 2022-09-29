import json

with open('users.json') as f:
    data = json.load(f)

largest_number = len(data[0]['friends'])

for persone in data:
    if len(persone['friends']) > largest_number:
        largest_number = len(persone['friends']) 
        print(json.dumps(persone, indent=2))

