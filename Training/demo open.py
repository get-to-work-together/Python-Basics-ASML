filename = 'data.txt'

# f = open(filename, mode='a')
# print('Peter', file = f)
# f.close()

with open(filename, mode='r') as f, open('out.txt', mode='w') as f_out:

    first_line = f.readline()
    print('first line:', first_line)

    for line in f:
        line = line.strip()
        if line.startswith('A'):
            print(line)
            print(line, file=f_out)

    f.seek(0)
    print('first line:', f.readline())
