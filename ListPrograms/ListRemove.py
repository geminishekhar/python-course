#Removing the element from the list
myList=[1,2,3,4,5,6,7,8]
myList.remove(1)
print(myList)

#Only one gets removed at a time if duplicates present
newList=[1,2,2,3,4,5,6,6,7,7]
newList.remove(2)
print(newList)
print(newList.pop())
print(newList.pop(5))

#Del keyword..
del newList[3]
print(newList)