import unittest

def cube(x):
    """Return the cube (power 3) of the argument
    """
    return x ** 3

class TestCube(unittest.TestCase):
    def test_simple(self):
        x = 5
        expected = 125
        actual = cube(x)
        self.assertEqual(expected, actual)
    def test_negative(self):
        x = -5
        expected = -125
        actual = cube(x)
        self.assertEqual(expected, actual)

# -------------------------

if __name__ == '__main__':

    x = 5
    expected = 126
    actual = cube(x)

    # assert actual == expected

    # if actual == expected:
    #     print('OK')
    # else:
    #     print('TEST FAILED')

    # import doctest
    # doctest.testmod(verbose=True)

    unittest.main()