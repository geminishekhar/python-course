#Variable inside the function is accessible beacuse it is termed as global ....
def func():
    global x
    x="Latech"

func()
print(x)

#To change the global variable using the function .....

y="BullDogs"
def myFunc():
    global y
    y="Titans"

myFunc()

print(y)

