fruits=["apple","mangoes","strawberry"]
print(fruits)

#allows duplicate values
myList=[1,2,2,1,2]
print(myList)

#Printing the length of the list
print(len(myList))

#type of the list
print(type(myList))

mixedList=[1,2,3,4.0,"cat",True,False]
print(type(mixedList))

# Printing the elements at a particular index.
print(mixedList[1])

#if item is present in the list
if 4.0 in mixedList:
    print("4.0 is present in the list." )
if "cat" in mixedList:
    print("cat is present in the list ")