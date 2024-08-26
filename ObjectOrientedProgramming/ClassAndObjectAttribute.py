class Person:
    name="Anonymous"
    def change_name(self,name):
        self.name="Jack"
        Person.name="Sam"


p1=Person()
p1.change_name("Sam")

print(p1.name)
print(Person.name)