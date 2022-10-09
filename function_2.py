x = 1
print (x)

def fn_print ():
    x = 10
    
print (fn_print())

print (x)
print ("-----------------------------------------")

def fn_main ():
    x = 10

    def fn_internal ():
        return 5


    return x + fn_internal()

print (fn_main())
print ("-----------------------------------------")


x = 0
print (bool(x))
print ("-----------------------------------------")
x = (1, 1, 1)
print(sum(x), min(x), max(x))

print ("-----------------------------------------")

def fn_factorial (n):
    if n == 0:
        return 1
    else:
        return n * fn_factorial (n-1)

print (fn_factorial (5))

print ("-----------------------------------------")

def fn_number (n):
    for i in range(1, n+1):
        print (i)


fn_number (5)
print ("-----------------------------------------")


def fn_s_rectangle (a, b):
    s = a * b
    return s

print(fn_s_rectangle(5, 10))

