print("------------------")
my_dict = {"key":'value', 10: "hello", 2: "bye"}
print(my_dict)
print (my_dict["key"])
print (my_dict.get("key"))
print (my_dict.get("key"), my_dict.get(10), my_dict.get(2), my_dict.get(1, 1) )
print(my_dict)
print (my_dict.items())
print (my_dict.pop(2))
print(my_dict)
my_dict = {"key":'value', 10: "hello", 2: "bye"}
print (my_dict.popitem())
print(my_dict)
my_dict = {"key":'value', 10: "hello", 2: "bye"}
print (my_dict.values())
my_dict.update({3: 777})
print(my_dict)
my_dict1 = {20:'v', 300: "ho", 400: "by"}
my_dict.clear()
my_dict.update(my_dict1)
print(my_dict)
print("------------------")

my_list = [1, 2, 1, 2, 3]
value_count = 1
count_dict = {value_count: 0}
for elem in my_list:
    if elem == value_count:
        count_dict[value_count] += 1
print (count_dict)
print("------------------")
my_list = [1, 2, 1, 2, 3]
count_dict = {}
for elem in my_list:
    if elem in count_dict:
        count_dict[elem] += 1
    else:
        count_dict[elem] = 1
for k, v in count_dict.items():
    print ("Key:", k, "count:", v)

print("------------------")
my_dict = {1: 10, 2: 20, 3: 30}
for k, v in my_dict.items():
    if k % 2 == 0:
        print ("Key:", k, "count:", v)

my_dict = {"c": 10, 'ab': 20, "d": 30}
my_dict_dop = {}
for k, v in my_dict.items():
    if k[0] != 'a':
        my_dict_dop[k] = v
print (my_dict_dop)
