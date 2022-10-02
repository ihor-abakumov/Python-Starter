print ("Exercise 1")
number_fib1 = 1
number_fib2 = 1
for number in range(98):
    if number_fib2 < 2:
        print (number_fib1)
        print (number_fib2)
    number_fib3 = number_fib2 + number_fib1
    number_fib1 = number_fib2
    number_fib2 = number_fib3
    print (number_fib2)
print ("------------")

print ("Exercise 2")
word = "Hello world"
for char in word:
    if char == "o":
        char = "a"
    if char == "l":
        char = "e"
    print (char)
print ("------------")

print ("Exercise 3")
word = "Hamaaa"
counter = 1
for char in word:
    if counter % 2 != 0:
        char = "_"
    elif char == "a":
        char = "b"
    print (char)
    counter += 1
print ("-----------")
