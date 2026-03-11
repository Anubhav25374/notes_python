#Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car():
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

my_car1 = Car("honda", "city")
print(my_car1.Brand)        
print(my_car1.Model) 

my_car2 = Car("honda", "venue")
print(my_car2.Model)
print(my_car2.b)