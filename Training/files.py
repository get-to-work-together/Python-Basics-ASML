import re

filename = 'names.txt'
filename = '/Users/peter/Lesgeven/Computrain/_InCompany/ASML/Python Basics/Training/names.txt'
filename = '~/Lesgeven/Computrain/_InCompany/ASML/Python Basics/Training/names.txt'
filename = '../../_InCompany/ASML/Python Basics/Training/names.txt'

# on windows
filename = 'C:\\Users\\peter\\Lesgeven\\Computrain\\_InCompany\\ASML\\Python Basics\\Training\\names.txt'
filename = r'C:\Users\peter\Lesgeven\Computrain\_InCompany\ASML\Python Basics\Training\names.txt'
filename = r'..\..\_InCompany\ASML\Python Basics\Training\names.txt'

filename_in = 'names.txt'
filename_out = 'selected_names.txt'

class EmptyLineException(Exception):
    pass



# # LBYL
# import os
# if not os.path.exists(filename):
#     print('File {} does not exist'.format(filename))
#     exit()

# EAFP
try:
    with open(filename_in) as file:
        lines = file.readlines()

    with open(filename_in, mode='r') as f_in:
        with open(filename_out, mode='w') as f_out:

            headers = f_in.readline().strip().split()
            for line in f_in:
                # if line.strip() == '':
                #     raise EmptyLineException('Empty line')
                line = line.strip().split()
                d = dict(zip(headers, line))
                if re.search(r'a..l', d['e-mail']):
                    print(';'.join(d.values()), file=f_out)

except FileNotFoundError:
    print('File {} does not exist'.format(filename))
    exit()

