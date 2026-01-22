import os
import pathlib
import logging

logging.basicConfig(level=logging.INFO)

# filename = 'commands.txt'
# filename = os.path.join(os.path.dirname(__file__), 'commands.txt')

filename = pathlib.Path(__file__).parent / 'commands.txt'


jump_table = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x // y,
    'mod': lambda x, y: x % y,
    'set': lambda x, y: y,
}

result = 0
logging.debug('initial => ' + str(result))

try:

    with open(filename) as f:
        for line in f:
            line = line.strip()
            operation, value = line.split()
            f = jump_table[operation]
            result = f(result, int(value))
            logging.debug(line + ' => ' + str(result))

except FileNotFoundError:
    print(f'File "{filename}" not found.')
    exit()

print(result)
