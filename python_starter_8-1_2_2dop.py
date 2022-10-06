# HW - 1
print ("---------------------")

def summa_int (a, b):
    if type(a) != int or type (b) != int:
        return None, 1
    elif a + b >= 0: 
        return a + b, 1
    elif a + b < 0: 
        return a + b, -1
    
    
sum_, code_ = summa_int (20, 0)
print (sum_)
print (code_)


# HW - 2
print ("---------------------")
def summa (a, b):
    return a + b
print (summa (5, 2))

def integral_func (any_func):
    return print("Start"), print (any_func), print("End")

integral_func (summa (10 ,20))

# Solo Work - 
# Function Algoritm Evklida 2 numbers
print ("---------------------")

def evklid_func (a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

print (evklid_func (2742245548560427017, 5944975256305754709))