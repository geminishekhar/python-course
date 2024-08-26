class Student:
    #Class Attribute
    University_name="Latech"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

#Object Attribute

s1=Student("Jack",50)
print(s1.University_name)
print(s1.name)
print(s1.marks)

