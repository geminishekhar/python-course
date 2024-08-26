class Student:
    name="Jack"
    roll_no=20

#cant access or change object or class Atrributes...
    @staticmethod
    def change_details(name,roll_no):
        Student.name=name
        print(Student.name)
        print(name)
        print(roll_no)


s1=Student()
#print(s1.name)
#print(s1.roll_no)
s1.change_details("John",100)