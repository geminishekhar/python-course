class Student:
    name="Jack"
    roll_no=23

    @classmethod
    def change_Details(cls,name,roll_no):
        cls.name=name
        cls.roll_no=roll_no

s1=Student()
print(s1.name)
print(s1.roll_no)
s1.change_Details("John",100)
print(s1.name)
print(s1.roll_no)