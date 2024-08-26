#inserting without replacing the existing element .....
myList=[10,20,30,40,50,60,70,80]
myList.insert(2,200)
print(myList)

#append the values
myList.append(500)
print(myList)

myNextList=[600,700,800,900]
myList.extend(myNextList)
print(myList)

#adding  tuple to the list
#Cant be vice versa
list1=[1,2,3,4,5]
tuple1=(6,7,8,9,10)
list1.extend(tuple1)
print(list1)
