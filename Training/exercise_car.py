class Car:

    def __init__(self, make, model, color, mileage=0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def info(self):
        s = f'My great {self._color} {self._make} {self._model} has driven {self._mileage}km.'
        s += f'\nThat\'s more than {self._mileage // 40075} times around the earth!'
        if self._mileage > 363104:
            s += f'\nThat\'s further than driven to the moon!'
        return s

    def drive(self, distance):
        self._mileage += distance


# ---------------------------------------------------------

my_car = Car('Renault', 'Megane Station', 'metalic brown', 508000)

my_car.drive(204)
my_car.drive(204)

print(my_car.info())
