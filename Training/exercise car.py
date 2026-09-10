from dataclasses import dataclass


class Car:

    def __init__(self,
                 make: str,
                 model: str,
                 color: str,
                 mileage: int = 0):
        self._make = make
        self._model = model
        self._color = color
        if mileage >= 0:
            self._mileage = mileage
        else:
            self._mileage = 0
            raise Exception('Invalid argument: Can instantiate with a negative mileage!')

    def __repr__(self):
        return f"Car(make='{self._make}', model='{self._model}', color='{self._color}', mileage={self._mileage})"

    def __str__(self):
        return f"I love this car make='{self._make}' model='{self._model}' color='{self._color}', mileage={self._mileage}"

    def drive(self, distance: int):
        if distance < 0:
            raise Exception('Invalid argument: Can not drive a negative distance!')
        self._mileage += distance

    def info(self) -> str:
        return f'This beautiful {self._color} {self._make} {self._model} has driven {self._mileage}km.'



# or

# @dataclass
# class Car:
#     make: str
#     model: str
#     color: str
#     mileage: int = 0
#
#     def drive(self, distance):
#         self.mileage += distance
#
#     def info(self):
#         return f'This beautiful {self.color} {self.make} {self.model} has driven {self.mileage}km.'

# ----------------------------------

if __name__ == '__main__':

    car1 = Car('Renault', 'Megane station', 'metalic brown', 520000)
    print(car1.info())

    print(str(car1))
    print(repr(car1))