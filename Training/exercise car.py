class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def drive(self, distance):
        if distance < 0:
            raise Exception('Cannot accept negative distance!')
        self._mileage += distance

    def info(self):
        print(f'This great {self._color} {self._make} {self._model} has driven {self._mileage} miles.')


# ---------------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane station', 'metalic brown', 485000)

    my_car.info()

    my_car.drive(211)
    my_car.drive(211)

    my_car.info()
