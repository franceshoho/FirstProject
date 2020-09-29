"""
Use class Car and Electric Car to make cars
"""
from car import Car  # import Car class and all its methods
from electric_car import ElectricCar  # import Electric Car in sep file

def main():
    # my_car = Car(color="black", make="Lexus", odometer=1000)
    # print("I'm a car!")
    # while True :
    #     action = input("What should I do? [A]ccelerate, [B]rake, \n"
    #                    "[Q]uit, [C]hange color, change [M]ake, \n"
    #                    "show [O]dometer, or show average [S]peed? ").upper()
    #     if action not in "ABOSQM" or len(action) != 1 :
    #         print("I don't know how to do that")
    #         continue
    #     if action == 'Q' :
    #         break
    #     if action == 'A' :
    #         my_car.accelerate()
    #     elif action == 'B' :
    #         my_car.brake()
    #     elif action == 'C':
    #         color = input("What color do you like? ")
    #         my_car.change_color(color)
    #     elif action == 'M':
    #         make = input("What make? ")
    #         my_car.change_model(make)
    #     elif action == 'O' :
    #         print("The car has driven {} kilometers".format(my_car.odometer))
    #     elif action == 'S' :
    #         print("The car's average speed was {} kph".format(
    #             my_car.average_speed()))
    #     my_car.step()
    #     my_car.say_state()
    #     my_car.describe()

    my_car = Car()
    my_car.describe()
    my_eCar = ElectricCar()
    my_eCar.describe()
    my_eCar.change_make('Porsche')
    my_eCar.describe()
    my_eCar.battery.change_battery(100, type='nickel')
    my_eCar.battery.range()

if __name__ == '__main__':
    main()


