# HW - 1
print ("------------------------------")

def fn_check_devision (a, b):
    try:
        return a/b
    except:
        print ("ZeroDivizionError")

if fn_check_devision(2, 0) == None:
    print ("Function - fn_check_devision - Error")


# HW - 2
print ("------------------------------")

def fn_check_number_list (fn_list,elem):
    try:
        return fn_list[elem]
    except:
        print ("Not this element in list")
        return -1

my_list = [1,2,3]
print (fn_check_number_list (my_list,3))