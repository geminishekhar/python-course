L1=[1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4]
L2=[]

index=0
while index<len(L1):
    if L1[index] in L2:
        index=index+1
    else:
        L2.append(L1[index])
        index=index+1

print(L2)


mydigit=234
result=0
while mydigit>0:
    rem=mydigit%10
    mydigit=mydigit//10
    result=result+rem
print(result)