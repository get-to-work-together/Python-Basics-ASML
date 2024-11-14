# names = []
#
# while True:
#     name = input('Enter a name: ')
#
#     if name == '':
#         break
#
#     names.append(name)
#
# for name in sorted(names):
#     print(name)

class InvalidArgumentException(Exception):
    pass


def calculate_area(width, height):
    # assert (width >= 0 and height >= 0), 'Invalid argument'

    if width < 0 or height < 0:
        raise InvalidArgumentException('Invalid argument')

    return width * height


try:
    area = calculate_area(10, -2)
    print(area)

except AssertionError as err:
    print(err)

except InvalidArgumentException as err:
    print(err)
