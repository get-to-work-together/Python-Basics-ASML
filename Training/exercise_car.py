class Car:

    __slots__ = ['make', 'model', 'color', 'year', 'mileage']

    def __init__(self, make, model, color, year, mileage = 0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def info(self):
        return f'My beautiful {self.color} {self.make} {self.model} from {self.year} has driven {self.mileage}km.'

    # def __str__(self):
    #     return f'Car - {self.color} {self.make} {self.model} from {self.year} has driven {self.mileage}km.'

    def __repr__(self):
        return f'Car({self.color}, {self.make}, {self.model}, {self.year}, {self.mileage})'

# ======================================================================

if __name__ == '__main__':

    car = Car('Renault', 'Megane Station', "metalic brown", 2013, 510000)

    print(car.info())
    car.drive(350)
    print(car.info())

    print(car)
    print(str(car))
    print(repr(car))
