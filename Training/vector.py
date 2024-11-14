from typing import Self
import math


class Fraction:

    def __init__(self, nominator:int=0, denominator:int=1):
        gcd = math.gcd(nominator, denominator)
        self._nominator = nominator // gcd
        self._denominator = denominator // gcd

    @staticmethod
    def parse(s):
        splited = s.split('/')
        nominator = int(splited[0].strip())
        denominator = int(splited[1].strip())
        return Fraction(nominator, denominator)

    def __repr__(self) -> str:
        return f'Fraction({self._nominator}, {self._denominator})'

    def __str__(self) -> str:
        return f'{self._nominator}/{self._denominator}'

    def __add__(self, other: Self) -> Self:
        common_denominator = self._denominator * other._denominator
        nominator1 = self._nominator * other._denominator
        nominator2 = other._nominator * self._denominator
        return Fraction(nominator1 + nominator2, common_denominator)

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Fraction(-self._nominator, self._denominator)

    def __mul__(self, other: Self) -> Self:
        return Fraction(self._nominator * other._nominator, self._denominator * other._denominator)

    def __truediv__(self, other: Self) -> Self:
        return Fraction(self._nominator * other._denominator, self._denominator * other._nominator)

    def __float__(self):
        return self._nominator / self._denominator

    def invert(self):
        return Fraction(self._denominator, self.nominator)


# -------------------------------------------------------------------------

if __name__ == '__main__':

    f1 = Fraction(4, 6)
    f2 = Fraction(1, 5)
    f3 = Fraction.parse('1/4')
    f4 = Fraction(4)


    print('f1 = ', f1)
    print('f2 = ', f2)
    print('f3 = ', f3)

    print('f1 + f2 = ', f1 + f2)
    print('f1 - f2 = ', f1 - f2)
    print('f1 * f2 = ', f1 * f2)
    print('f1 / f2 = ', f1 / f2)

    print(float(f1))
    print(float(f2))
    print(float(f3))