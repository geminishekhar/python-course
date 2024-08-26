myList=[1,1,1,2,2,3,4,4,4,4,4,5,6,6,6]
occurence={}
for x in myList:
    if x in occurence:
        occurence[x]+=1
    else:
        occurence[x]=1

print(occurence)

#Highest occurence of a particular element
max=-1
for x in occurence.values():
    if x>max:
        max=x
print(max)