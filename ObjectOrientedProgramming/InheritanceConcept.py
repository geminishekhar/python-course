class Car:

    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

class Toyota(Car):
    def __init__(self,name):
        self.name=name

car1=Toyota("Fortuner")
car1.start()

