filename = 'data.txt'

filename = '/Users/peter/Lesgeven/Computrain/_InCompany/ASML/Python Basics/Training/data.txt'

with open(filename) as f:

    for line in f.readlines():
        line = line.strip()

        if 'r' in line.lower():
            print(line)

