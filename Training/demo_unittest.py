
def square(n):
    """Calculate the square

    >>> square(2)
    4

    >>> square(100)
    10000

    >>> square(0)
    0
    """
    return n ** 2


# ----------------------------------------------

import unittest
class TestFunction(unittest.TestCase):

    def test_multiple(self):
        numbers = [0, 2, 100]
        actual = [square(n) for n in numbers]
        expected = [0, 4, 10000]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()



    # import doctest
    # doctest.testmod(verbose=True)


    # expected = 5
    # actual = square(2)
    # assert expected == actual, 'Error'
    #
    # expected = 10000
    # actual = square(100)
    # assert expected == actual, 'Error'
    #
    # expected = 0
    # actual = square(0)
    # assert expected == actual, 'Error'

    # print(square(2))   # 4
    # print(square(100))  #  10000
    # print(square(0))    # 0





# def square(n):
#     """Calculate the square of n.
#
#     >>> square(4)
#     16
#     >>> [square(n) for n in range(6)]
#     [0, 1, 4, 9, 16, 25]
#     """
#     return n ** 2
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
