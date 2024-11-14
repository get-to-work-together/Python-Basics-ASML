class Car:

    distance_unit = 'miles'

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def drive(self, distance):
        self._mileage += distance

    def info(self):
        return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}{Car.distance_unit}.'


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault',
                 'Megane',
                 'metalic brown',
                 466000)

    print(my_car.info())

    my_car.drive(242)
    my_car.drive(242)

    print(my_car.info())
