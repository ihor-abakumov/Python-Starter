counter = 5
while counter > 0:
    print ("Iteration, counter =", counter)
    counter -= 1
print ("-----------")
print (counter)
print ("-----------")

for number in range(5):
    print (number)
print ("-----------")

for number in range(10):
    if number == 2:
        continue
    if number == 5:
        break
    print (number)

print ("-----------")
for number in range (101):
    if number % 2 == 0:
        print (number)
print ("-----------")

counter = 0
end_value = 101 
while counter <= end_value:
    if counter % 2 == 0:
        print (counter)
    counter += 1
print ("-----------")

word = "hello"
for char in word:
    if char == "l":
        print("s")
    else:
        print (char)
print ("-----------")


counter = 96
end_value = 0 
while counter >= end_value:
    if counter % 5 == 0:
        print (counter)
    counter -= 1
