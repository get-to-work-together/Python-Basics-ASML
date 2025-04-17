import unittest


def cube(x: int|float) -> int|float:
    """Calculate the cube (power of 3) of a number

    >>> cube(3)
    27

    >>> cube(4)
    64

    >>> cube(0)
    0
    """
    return x ** 3



# ----------------


class TestCube(unittest.TestCase):

    def test_simple(self):
        actual = cube(4)
        expected = 64
        self.assertEqual(expected, actual)

    def test_zero(self):
        actual = cube(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_negative(self):
        actual = cube(-3)
        expected = -27
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()