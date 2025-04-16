from copy import deepcopy

letters = ['A','B','C']
names = ['Daan', 'Joost', 'Peter', 'Siyuan', letters]

copy = deepcopy(names)

names.pop()