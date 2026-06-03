filename = 'email.txt'
# filename = '/Users/peter/Lesgeven/Computrain/_InCompany/ASML/Python Basics/Training/email.txt'
# filename = r'..\Training\email.txt'


filename_out = 'selected_email.txt'

try:
    with open(filename) as f, open(filename_out, mode='w') as f_out:

        header = f.readline()
        headers = [s.strip() for s in header.split(',')]

        for line in f:
            line = line.strip()
            values = [s.strip() for s in line.split(',')]

            d = dict(zip(headers, values))

            if d['E-MAIL'].endswith('@asml.com'):
                print(line, file=f_out)
            else:
                print(line)

except FileNotFoundError:
    print(f'File "{filename}" does not exist.')
