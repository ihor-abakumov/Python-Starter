from typing import List


my_list = list("a1Truecd")
print(my_list)
my_list = ["l", 1, True]
my_list2 = list(my_list)
print(my_list)
print(my_list2)
print(my_list[1:2])

my_list = [1, 2, 3, 4 ,5]
my_list.append(10)
print (my_list)
my_list = [1, 2]
my_list.append(3)
print (my_list)
my_list.clear()
print (my_list)
print ("------------------")

my_list = [1, 2, 3, 4 ,5]
my_list_ext = [5, 4, 3, 2, 1]

my_list.append(10)
print (my_list)
my_list.extend(my_list_ext)
print (my_list)
print (my_list.index(3))
my_list += my_list_ext
print (my_list)
my_list_remove = my_list.pop(5)
print (my_list_remove)
my_list = [1, 2, 3]
my_list.reverse()
print (my_list)
my_list = [5, 2, 1, 4 ,3]
my_list.sort()
print (my_list)
my_list = [5, 2, 1, 4 ,3]
my_list.sort(reverse = True)
print (my_list)

my_list = [5, 2, 1, 4 ,3]
for elem in my_list:
    print (elem)
print("-----------------")

my_list = [5, 2, 1, 4 ,3]
dop_list = []
for elem in my_list:
    if elem % 2 != 0:
        dop_list.append(elem)
print (dop_list)

print("-----------------")

my_list = [5, 2, 1, 4 ,3]
dop_list = []
for elem in my_list:
    dop_list.append(elem ** 2)
print (dop_list)

print("-----------------")

my_list = [5, 2, 1, 4 ,3]
elem_max = my_list [0]
for elem in my_list:
    if elem > elem_max:
        elem_max = elem
print (elem_max)

my_list = [5, 2, 1, 4 ,3]
elem_min = my_list [0]
for elem in my_list:
    if elem < elem_min:
        elem_min = elem
print (elem_min)

print([1, 2, 3, 4, 5][1:3])