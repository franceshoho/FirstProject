"""
Class Electric Car - subclass of Car (from car.py)
"""
from car import Car

# subclass needs class Name inside () ex subclass(Car)

# a separate class just for Battery, unrelated to Car or ElectricCar
class Battery:
    def __init__(self, size=75):
        self.size = size    # initiate battery size
        self.type = 'lithium'

    def change_battery(self, size, type='lithium'):
        self.battery = size
        self.type = type
        print("Battery is now", type, "of size", size, "kwh")

    def range(self):
        if self.battery == 75:
            range = 260  # you can use regular range, which isn't an attr
            # to class, esp. you won't be reusing it
        else:
            range = 350
        print(f'This car can go {range} miles on a full charge.')


# subclass - Electric Car, needs Car in () to inherit attrs
class ElectricCar(Car):
    # first need to initiate parent class Car with all necessary attr
    # then use super() to initiate child class again with all
    # necessary attrs
    def __init__(self, speed=0, odometer=0, color="blue"):
        super().__init__(speed, odometer, color)
        self.make = 'Tesla'  # make default make as Tesla, not Toyota
        self.battery = Battery()  # create using Battery class

    # this overrides describe() from parent Car class above
    def describe(self):
        if self.make :
            print(f'This is electric car is a '
                  f'{self.color} {self.make}.')
        else :
            print(f'This electric car is {self.color}.')


