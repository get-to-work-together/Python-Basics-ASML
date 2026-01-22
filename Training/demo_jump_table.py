commands = [
    'add 10',
    'sub 3',
    'mul 2',
    'div 2',
]

jump_table = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

result = 0
for command in commands:
    print(command, end=' => ')
    operation, value = command.split()
    f = jump_table[operation]
    result = f(result, int(value))
    print(result)