import json

def install_sort(package):
    return package['age']

with open('users.json') as f:
    data = json.load(f)

data.sort(key=install_sort)

data_str = json.dumps(data, indent=2)

print(data_str)