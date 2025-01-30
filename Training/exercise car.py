class Car:

    distance_unit = 'km'

    __slots__ = ['_make', '_model', '_color', '_mileage']

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def __del__(self):
        print('Your car has been demolished!!!')

    def __repr__(self):
        return f'Car("{self._make}", "{self._model}")'

    @staticmethod
    def convert_miles_to_kilometers(miles):
        return 1.6 * miles

    def drive(self, distance):
        if distance < 0:
            raise Exception('Cannot accept negative distance!')
        self._mileage += distance

    def info(self):
        print(f'This great {self._color} {self._make} {self._model} has driven {self._mileage} {Car.distance_unit}.')


# ---------------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane station', 'metalic brown', 485000)

    my_car.info()

    my_car = Car('Renault', 'Clio', 'red', 0)

    my_car.drive(211)
    my_car.drive(211)

    my_car.info()

    print(my_car)

