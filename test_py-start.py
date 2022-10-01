product_price = 700
str_ = ""

if product_price > 1000:
    product_price *= 0.9
elif product_price > 500:
    product_price *= 0.95
elif product_price > 100:
    product_price *= 0.97
print (product_price)

print (None if not str_ else str_)
