#HW - 1, 2, 3
a = {3, 5, 11, 7, 4, -3}
b = {11, 5, 8, 1, 10, 7}
print ("-------------------------")
print (a.difference(b))
print (a.intersection(b))
print (a.union(b))

#HW - 4
a = "Igor"
my_list = list(a)
my_set = set (a)

if len (my_list) == len (my_set):
    print ("unical")
else:
    print ("no unical")
