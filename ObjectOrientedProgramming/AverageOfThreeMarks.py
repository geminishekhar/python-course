class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average_marks(self):
        sum=0
        for x in self.marks:
            sum=sum+x
        average=sum/3
        print(f" Hey {self.name} your average is three subjects is :",average)

    #Class Level Method......
    @staticmethod
    def Hello():
        print("Hello")

s1=Student("John",[93,92,94])
s1.average_marks()
s1.Hello()