def yieldFunction():
    i=0
    while i<10:
        yield i
        i+=1

x=yieldFunction()
print(next(x))
print(next(x))
print(next(x))
print(next(x))