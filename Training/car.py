
class Car:
    """My Car class"""

    def __init__(self, make, model, year, color, mileage = 0):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._mileage = mileage

    def __repr__(self):
        return f'Car - make:{self._make}, model:{self._model}'

    def __str__(self):
        return f'My Car is a {self._make} {self._model} from {self._year}'

    def info(self):
        return f'My beautiful {self._color} {self._make} {self._model} from {self._year} has driven {self._mileage}km.'

    def drive(self, distance):
        self._mileage += distance

# ---------------------------------------------

my_old_car = Car(make = 'Renault',
                 model = 'Megane stationwagon',
                 year = 2002,
                 color = 'metalic brown',
                 mileage = 545000)

my_old_car.drive(220)
my_old_car.drive(220)

print(my_old_car.info())

print(str(my_old_car))
print(repr(my_old_car))
