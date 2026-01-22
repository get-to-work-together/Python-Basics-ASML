filename = '/Users/peter/Lesgeven/Computrain/_InCompany/ASML/Python Basics/Training/data.txt'
filename = '../Training/data.txt'

filename = '..\\Training\\data.txt'
filename = r'..\Training\data.txt'

filename = r'C:\Users\peter\Lesgeven\Computrain\_InCompany\ASML\Python Basics\Training\data.txt'

filename = 'data.txt'


import os
print(os.getcwd())

print(__file__)
print(os.path.dirname(__file__))
filename = os.path.join(os.path.dirname(__file__), 'data.txt')
print(filename)

import pathlib
filename = pathlib.Path(__file__).parent / 'data.txt'
print(filename)



with open(filename) as f:
    headers = [v.strip() for v in f.readline().strip().split(',')]
    for line in f:
        line = line.strip()
        values = [v.strip() for v in line.split(',')]
        d = dict(zip(headers, values))
        if d['city'] in ('Eindhoven', 'Veldhoven'):
            print(line)
