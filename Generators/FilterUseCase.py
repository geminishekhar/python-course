marks=[32,42,50,60,75,80,90]

def failinggrades(marks):
    return marks<60

failing=filter(failinggrades,marks)
print(next(failing))
print(next(failing))
print(next(failing))
