myList=[1,2,3,4,5,5,6,6,7,7,8,8,9,9]
# By Default it is an dictionary mySet={}
# To create an empty Set , use mySet=set()
mySet=set()
newListDuplicates=[]
for x in myList:
    if x in mySet:
        newListDuplicates.append(x)
    else:
        mySet.add(x)

print(newListDuplicates)
