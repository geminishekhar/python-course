class Car:

    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

class Toyota(Car):
    def __init__(self,EngineType):
        self.EngineType=EngineType

class Fortuner(Toyota):
    def __init__(self,name):
        self.name=name

car1=Fortuner("Fortuner1")
car1.EngineType="Diesel"
print(car1.EngineType)
