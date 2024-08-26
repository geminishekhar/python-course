class Student:
    name="anonymous"
    def change_Name(self,name):
        self.name=name

s1=Student()
s1.change_Name("Sam")

print(s1.name)
print(Student.name)