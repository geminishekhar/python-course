myNumber=123443217899
myMap={}

while(myNumber>0):
    rem=myNumber%10
    if rem in myMap:
        myMap[rem]=myMap[rem]+1
    else:
        myMap[rem]=1
    myNumber=myNumber//10

print(myMap)
