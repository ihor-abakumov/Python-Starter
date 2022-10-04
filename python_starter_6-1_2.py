# HW - 1

d = {"a": 3, "b": 0, "c": 4, "d": -3}

# This is the only way to think out 1 meaning from the dictionary
for i in d.values():
    value_max = i
    break

for value in d.values():
    if value >= value_max:
        value_max = value
print ("Max value in dictionary:", value_max)
print ('------------------------')

# HW - 2

d = {"a": 4, "b": "hello", "c": 5, "d": -3}

# This is the only way to think out 1 meaning from the dictionary
for i in d.values():
    if type(i) == str:
        continue
    else:
        value_max = i
        break

for value in d.values():
    if type(value) == str:
        continue
    elif value >= value_max:
        value_max = value
print ("Max value in dictionary:", value_max)
print ('------------------------')