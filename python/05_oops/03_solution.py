#Create an ElectricCar class that INHERITS from the Car class and has an additional attribute battery_size.

class Car():
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

    def full_name(self):
        return f"{self.Brand} {self.Model}"   
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.Battery_life = battery_life    

my_tesla = ElectricCar("tesla", "model S", "85KWH") 
print(my_tesla.Model)       
print(my_tesla.Brand)   
print(my_tesla.full_name())    