class Student:
    def __init__(self,name):
        self.name=name
        print(f"my name is {self.name}")
        print(self)

s1=Student("John")
print(s1)