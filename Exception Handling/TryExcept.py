num1=10
num2=10
try:
    div=num1/num2
    print(di)
except ZeroDivisionError:
    print("there is an zero division error,please correct it.")
except NameError:
    print("Variable name is wrong..")

print("rest of the code...")