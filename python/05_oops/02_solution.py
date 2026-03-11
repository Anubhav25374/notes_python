#Add a method to the Car class that displays the full name of the car (brand and model).

class Car():
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

    def full_name(self):
        return f"{self.Brand} {self.Model}"    

my_car1 = Car("honda", "city")
print(my_car1.full_name())         

my_car2 = Car("honda", "venue")
print(my_car2.full_name())         
