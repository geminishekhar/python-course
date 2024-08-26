class Student:
    #Class Attribute
    University_name="Latech"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def myMethod(self):
        print("Hello",self.name)
#Object Attribute
    def get_marks(self):
        return self.marks

s1=Student("Jack",50)
print(s1.University_name)
print(s1.name)
print(s1.marks)
s1.myMethod()
print(s1.get_marks())

