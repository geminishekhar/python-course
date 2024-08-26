a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))

if a+b>=c or b+c>=a or a+c>=b:
    print("Triange")
else:
    print("Not a triangle")