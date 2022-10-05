my_set = {1, 2, 3, 4, 5}
my_set1 = {3, 8}
print (my_set)
print (my_set.pop())
my_set.discard(2)
print (my_set.add (1))
print(my_set.union(my_set1))
print (my_set.intersection(my_set1))
print (my_set)
print (my_set1.difference(my_set))
print (1 in my_set)

print ("-------------------------")
my_tuple = (1, 2, 3)
print (my_tuple)
x, y, z = my_tuple
my_tuple = z, y, x
print (my_tuple)

a = [(1, 2), (3, 4)]
for first, second in a:
    print (first, second)
    c, d = second, first
    print (c)
