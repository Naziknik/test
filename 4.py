from datetime import datetime
import json
import random


with open('users.json') as f:
    data = json.load(f)

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

full_name=random.choice(first_names)+" "+random.choice(last_names)
new_friend = {
    "id": random.randrange(3, 10),
    "name": full_name,
    "age": random.randrange(1, 99)
}

for persone in data:
    persone['balance'] = 0 
    persone['guid'] = "valid value"
    integer = persone['index'] / 3
    if persone['isActive'] == False:
        del persone['phone']
    if integer.is_integer():
        persone['friends'].append(new_friend)

with open(f'users_{datetime.now():%Y-%m-%d %H_%M_%S}_.json', 'w') as f:
    json.dump(data, f, indent=2)

# print(json.dumps(data, indent=2))

