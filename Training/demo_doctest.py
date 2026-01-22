def square(n: int):
    """Calculate the square of n.

    # >>> square(4)
    # 16
    # >>> [square(n) for n in range(6)]
    # [0, 1, 4, 9, 16, 25]
    """

    return n ** 2

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)

    assert square(4) == 16
