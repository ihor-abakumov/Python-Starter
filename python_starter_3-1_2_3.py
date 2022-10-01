# HW - 1
value = 10
print ("Even number") if value % 2 == 0 else print("Odd number")

# HW - 2
cat = "Bark"
if cat == "Meow":
    print ("This is a cat.")
elif cat == "Bark":
    print ("This is a dog.")
else:
    print ("Unknown beast.")

# HW - 3
value = 2
if value == 0:
   print ("Number is 0")
elif value < 0:
    if value > -10:
        print ("A definite negative number")
    elif value > -100:
        print ("Two digit negative number")
    elif value > -1000:
        print ("Three digit negative number")
    elif value <= -1000:
        print ("Four and more digit negative number")
else:
    if value < 10:
        print ("A definite positive number")
    elif value < 100:
        print ("Two digit positive number")
    elif value < 1000:
        print ("Three digit positive number")
    elif value >= 1000:
        print ("Four and more digit positive number")


