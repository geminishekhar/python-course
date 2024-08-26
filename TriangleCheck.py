a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))

if a==b and b==c and a==c:
    print("Equilateral Triangle")
elif a==b or b==c or a==c :
    print("Isosceles Triangle")
else:
    print("Scale Triangle")