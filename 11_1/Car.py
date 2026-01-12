class CAR:
    def __init__(self,owner,color, model, year):
        self.owner = owner
        self.color = color
        self.model = model
        self.year = year
    def print_owner(self):
        return f"The owner of the car is {self.owner}"
    def car_drive(self):
        return f"The {self.color} {self.model} of {self.owner} is driving"
    def car_stop(self):
        return f"The {self.color} {self.model} of {self.owner} has stopped moving"
    def car_fuel(self):
        return f"The {self.color} {self.model} of {self.owner} is refueling"
my_car = CAR("Alice", "red", "Toyota", 2020)
print(my_car.print_owner())
print(my_car.car_drive())
print(my_car.car_stop())            
print(my_car.car_fuel())