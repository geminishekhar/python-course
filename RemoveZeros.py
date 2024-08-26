

myList1=[2,0,0,0,3,4,5,0,0,6]
index=0

while index<len(myList1):
    if myList1[index]==0:
        myList1.remove(myList1[index])
    index=index+1
print(myList1)