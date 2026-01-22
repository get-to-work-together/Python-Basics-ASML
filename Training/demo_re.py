import re

filename = 'data.txt'

with open(filename) as f:
    for line in f:
        line = line.strip()
        match = re.search(r'Eindhoven.*?(\w+@asml\.\w{2,3})', line)
        if match:
            print(match.group(0))
            print(match.group(1))
