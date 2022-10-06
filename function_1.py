def print_sum ():
    print (2+2)

def func (a):
    print (2 * a)

def print_s (b):
    print (b)

def func1 (a, b, c):
    print (2 * a + b +c)

def func2 (a, b):
    return a*b

def get_max_from_list(list_values):
    max_value = list_values[0]
    for i in list_values:
        if i > max_value:
            max_value = i
    return max_value if max_value > 0 else "Max value is less then zero"

def get_string_length (string):
    return len(string)

def power (a,b):
    return a**b if b >= 0 else "Stepen is negative"


my_list = [-1, -2, -3]
my_string = "Igora"
print (get_max_from_list(my_list))
print (get_string_length(my_string))
print (power(-2,0))
print ("--------------------------")
    

print_sum()
func(5)
func("zzz-")
print_s (5)
print_s ("hello")
func1 (2, 1, 1)
print(func2 (2, 2))