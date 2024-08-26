#Printing the fruits with a letter present in it .
fruits=["apple","mango","cherry"]
newFruits=[]
for x in fruits:
    if "a" in x:
        newFruits.append(x)
print(newFruits)

#Printing only even numbers
myNumbers=[0,1,2,3,4,5,6,7,8,9,10]
evenNumbers=[]
evenNumbers1=[]
for x in myNumbers:
    if x%2==0:
        evenNumbers.append(x)
print(evenNumbers)

#More comprehensive way to do it .....
evenNumbers1=[x for x in myNumbers if x%2==0]
print(evenNumbers1)

myNumbers=[x for x in range(10)]
print(myNumbers)