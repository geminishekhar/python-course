myList=["apple","mango","carrot","cabbage","cabbage","apple","apple"]
myMap={}

for x in myList:
    if x in myMap:
        myMap[x]=myMap[x]+1
    else:
        myMap[x]=1
print(myMap)

max=-1
for x in myMap.values():
    if x>max:
        max=x

print(max)