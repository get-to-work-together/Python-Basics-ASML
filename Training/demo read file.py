filename = 'data.txt'
filename_out = 'export.txt'

with open(filename, mode='r') as f, open(filename_out, mode='a') as f_out:
    for line in f:
        line = line.strip()
        if line.startswith('B'):
            print(line, file = f_out)
