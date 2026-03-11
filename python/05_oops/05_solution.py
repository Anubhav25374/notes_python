#Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car():
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

    def full_name(self):
        return f"{self.Brand} {self.Model}"

    def fuel_tyoe(self):
        return "Diesel"   
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.Battery_life = battery_life  

    def fuel_tyoe(self):
        return "Battery"      

my_tesla = ElectricCar("tesla", "model S", "85KWH")
my_safari = Car("Tata", "Safari") 

print(my_tesla.fuel_tyoe())
print(my_safari.fuel_tyoe())