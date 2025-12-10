import os

filename = './Sandbox/ca-500.csv'

try:
    if not os.path.exists(filename):
        print('Cannot find file.')

    else:

        with open(filename) as f:
            headers = f.readline().rstrip('\n').split(';')
            for line in f:
                columns = line.rstrip('\n').split(';')
                d = dict(zip(headers, columns))
                if d['city'] == 'Montreal':
                    print('{:15} {:15} {:20} {:30}'.format(
                          d['first_name'],
                          d['last_name'],
                          d['city'],
                          d['email']))


except FileNotFoundError:
    print(f'File "{filename}" could not be found!')

except KeyError:
    print(f'Key error!')

# except Exception as ex:
#     print('Something went wrong!!!')
#     print(ex)