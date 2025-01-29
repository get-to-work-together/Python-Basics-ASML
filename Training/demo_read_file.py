# Mac OS or Linux
filename = 'data.txt'
filename = 'xxx/Users/peter/Computrain/_InCompany/ASML/Python Basics/Training/data.txt'

filename_out = 'errors.txt'

# Windows
# filename = 'C:\\Users\\peter\\Computrain\\_InCompany\\ASML\\Python Basics\\Training\\data.txt'
# filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Training\data.txt'

import os
if not os.path.exists(filename):
    print(f'File "{filename}" does not exist.')
    exit()

try:
    with open(filename, mode='r') as f:
        with open(filename_out, mode='w') as f_output:

            header_line = f.readline().strip()
            headers = header_line.split(',')

            total = 0.0
            number_of_errors = 0
            for line in f.readlines():
                line = line.strip()
                values = line.split(',')

                d = dict(zip(headers, values))

                if d['status'] == 'error':
                    number_of_errors += 1
                    print(line)
                    print(line, file=f_output)
                else:
                    fields = line.split(',')
                    value = float(d['var2'].strip())
                    total += value

    print(f'Number of errors = {number_of_errors}')
    print(f'The total of the values = {total}')


except FileNotFoundError:
    print(f'Cannot find file "{filename}".')

