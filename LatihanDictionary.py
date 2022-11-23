a = {}
b = {'n1': 100, 'n2': 90}

print(b['n1'])
print(b.keys())
print(b.values())
print(b.items())

b['n1'] = 200

print(b['n1'])

b['n3'] = 300

print(b.items())

for item in b.items():
    print(item)
