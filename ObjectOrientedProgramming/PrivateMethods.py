class Student:
    __university="Latech"
    #cant call the private function
    def __hello(self):
        print("Hello , welcome to the university.....")

    #need to write another function which can call the private function inside the same class....
    def welcome(self):
        self.__hello()



s1=Student()
s1.welcome()
