
filename = 'data.txtX'
# filename = '../Training/data.txt'
# filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Training/data.txt'
# filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Training\data.txt'
# filename = 'C:\\Users\\peter\\Computrain\\_InCompany\\ASML\\Python Basics\\Training\\data.txt'


try:
    with open(filename, mode='r') as f:

        first_line = f.readline().strip()
        headers = first_line.split(',')
        print(first_line[3:])

        print(20*'-')

        for line in f:
            line = line.strip()
            values = line.split(',')
            d = dict(zip(headers, values))
            if d['residence'] == 'Eindhoven':
                print(d['name'], d['residence'])

except FileNotFoundError:
    print(f'Cannot find file {filename}!')
