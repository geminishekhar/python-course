class Car:
    def __init__(self,type_Of_Car):
        self.type_Of_Car=type_Of_Car

    def start(self):
        print("Car Started.....")

    def stop(self):
        print("Car Stopped.....")

class Toyota(Car):
    def __init__(self,engine_type,type_Of_Car):
        super().__init__(type_Of_Car)
        self.engine_type=engine_type


car1=Toyota("Diesel","Electric")
#car1.type_Of_Car="Electric"
print(car1.type_Of_Car)