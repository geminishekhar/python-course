def myfunc():

    global a
    global b
    a = 7
    b = 8

a = 2
b = 3
myfunc()
print(a, b)