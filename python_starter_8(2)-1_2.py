# HW - 1

x = 1
print (x)


def fn_x (a):
    a = a + 10
    return a
    
x = fn_x (x)

print (x)
print ("-----------------------------------------")

# HW - 2

def fn_factorial (n):
    if n == 0:
        return 1
    else:
        return n * fn_factorial (n-1)

number_factorial = 5
print (number_factorial, "! =", fn_factorial(number_factorial))

print ("-----------------------------------------")
