# https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes

#OOP Exercise 1: Create a Class with instance attributes
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage


v1=Vehicle(240,10)
print("The max speed is ",v1.max_speed," and milage of the vechile is ",v1.mileage)
        
#OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle:
    pass

#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
        
