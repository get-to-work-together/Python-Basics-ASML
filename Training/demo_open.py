import os

filename = 'data.txt'
# filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Training/data.txt'
# filename = 'C:\\Users\\peter\\Computrain\\_InCompany\\ASML\\Python Basics\\Training\\data.txt'
# filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Training\data.txt'

def read_file(filename, keyword=''):
    with open(filename, mode='r') as f:
        for line in f:
            line = line.strip()
            if keyword in line:
                yield line


# -----------------

output_filename = 'results.txt'

with open(output_filename, mode='a') as f:
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            if filename == output_filename:
                continue
            for line in read_file(filename, keyword='is'):
                # f.write(line + '\n')
                print(filename, ':', line, file=f)
                print(filename, line)
