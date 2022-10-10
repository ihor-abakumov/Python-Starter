a = 10
b = 0
try:
    c = a /b
except:
    print ("division zero")

def x():
    g=10

try:
    print (g)
except NameError as error:
    print(error)
except ValueError as error:
    print(error)

try:
    print (int("abc"))
    assert 2 == 3
except ValueError as error:
    print(error)
except AssertionError as error:
    print(error)

print("----------------------------")
def get_mohtn(number):
    month = {1: "Jan", 2: "Feb"}
    try:
        return month[number]
    except :
        print("Data Error")

month_name = get_mohtn(8)
print (month_name)

print("----------------------------")
def check (sequence):
    if len (set(sequence)) == len (sequence):
        return True
    else:
        return False

def ch (array):
    try:
        return check (array)
    except:
        print("Data Error 2")

ddd = 1
print (ch(ddd))

    
