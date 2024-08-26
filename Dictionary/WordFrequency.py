sentence = "the quick brown fox jumps over the lazy dog the dog barks"
vowels=["a","e","i","o","u"]
myMap={}
for x in sentence:
    if x in vowels:
        if x in myMap:
            myMap[x]=myMap[x]+1
        else:
            myMap[x]=1

print(myMap)
