class Car:

    def __init__(self, speed=0, odometer=0, color="blue"):
        # speed, odomoneter and color have default values unless
        # users pass in explicitly a value, but they don't have to
        # make is optional arg (when arg="" or None)
        # time - you cannot control time, and it's accessible only
        # within class

        self.speed = speed
        self.odometer = odometer
        self.color = color
        self.time = 0
        self.make = 'Toyota'

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        # if self.time != 0:
        #     return self.odometer / self.time
        # else:
        #     pass
        if self.time != 0 :
            return self.odometer / self.time

    def change_color(self, color):
        self.color = color
        return self.color

    def change_make(self, make):
        self.make = make
        return self.make

    def describe(self):
        if self.make:
            print(f'This car is a {self.color} {self.make}.')
        else:
            print(f'This car is {self.color}.')





