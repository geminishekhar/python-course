class Student:
    name="Jack"
    #name and roll_no are objects attribute
    #created only when the object is created ....
    def __init__(self,name,roll_no):
        Student.name=name
        self.roll_no=roll_no

s1=Student("John",23)
print(s1.name)
print(Student.name)
print(s1.roll_no)

