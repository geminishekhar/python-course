List1=[1,2,3,4,5]
List2=List1
print(List1)
print(List2)
List1.append(6)
print(List1)
print(List2)
List2.append(7)
print(List1)
print(List2)

for x in List2:
    if x%2==0:
        print(x)