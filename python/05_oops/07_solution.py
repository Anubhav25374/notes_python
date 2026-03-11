#Add a static method to the Car class that returns a general description of a car.

class Car():
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model
    def full_name(self):
        return f"{self.Brand} {self.Model}"
    def fuel_tyoe(self):
        return "Diesel"   
    @staticmethod
    def general_des():
        return "Cars are fast"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.Battery_life = battery_life  

my_car = Car("Tata", "Safari")
Car("tata", "nexes")


print(my_car.general_des())        
print(Car.general_des())        