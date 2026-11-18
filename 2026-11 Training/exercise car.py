from dataclasses import dataclass


class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        if mileage >= 0:
            self._mileage = mileage
        else:
            raise Exception('Invalid argument: Can not instantiate with a negative mileage!')

    def drive(self, distance: int):
        if distance < 0:
            raise Exception('Invalid argument: Can not drive a negative distance!')
        self._mileage += distance

    def info(self):
        return f'This beautiful {self._color} {self._make} {self._model} has driven {self._mileage}km.'

    def __repr__(self):
        return f"Car(make='{self._make}', model='{self._model}', color='{self._color}', mileage={self._mileage})"

    def __str__(self):
        return 'A Car instance'

# or

# @dataclass
# class Car:
#     make: str
#     model: str
#     color: str
#     mileage: int = 0
#
#     def drive(self, distance: int):
#         if distance < 0:
#             raise Exception('Invalid argument: Can not drive a negative distance!')
#         self.mileage += distance
#
#     def info(self):
#         return f'This beautiful {self.color} {self.make} {self.model} has driven {self.mileage}km.'


# ----------------------------------

if __name__ == '__main__':

    car1 = Car(make='Renault', model='Megane station', color='metalic brown', mileage=520000)
    print(repr(car1))

    print(car1.info())
    car1.drive(424)
    print(car1.info())

    print(str(car1))
    print(repr(car1))
