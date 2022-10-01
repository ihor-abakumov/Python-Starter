product_price = 700

str_ = ""

first_value = 10
second_value = 0
operator = "/"

if first_value == None or second_value == None:
   print("Can't divide None value")
elif operator == "+":
    print (first_value + second_value)
elif operator == "-":
    print (first_value - second_value)
elif operator == "*":
    print (first_value * second_value)
elif operator == "/":
    if second_value == 0:
        print ("Can't divide by 0")
    else:
        print (first_value / second_value)
else:
    print("Operator is wrong. Choose from given: + - * /")    

if product_price > 1000:
    product_price *= 0.9
elif product_price > 500:
    product_price *= 0.95
elif product_price > 100:
    product_price *= 0.97
print (product_price)

print (None if not str_ else str_)


