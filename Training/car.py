
class Car:
    """My Car class"""

    distance_unit = 'miles'

    def __init__(self, make, model, color, year, mileage = 0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def info(self):
        """Prints car information"""
        print('My beautiful {} {} {} from {} has a mileage of {} {}'.format(self.color,
                                                                            self.make,
                                                                            self.model,
                                                                            self.year,
                                                                            self.mileage,
                                                                            Car.distance_unit))

    def drive(self, distance):
        """Drives car based on distance"""
        assert distance >= 0, 'Cannot drive a negative distance'
        self.mileage += distance


# ----------------------------------------------------------

my_car = Car('Renault', 'Megane station', 'metalic brown', 2013, 525000)

my_car.info()
my_car.drive(266)
my_car.drive(266)
my_car.info()

# my_car.drive(-10000)
# my_car.info()
