import os


print(os.getcwd())


filename = 'data.csv'
filename_out = 'out.txt'

with open(filename) as f:
    with open(filename_out, mode='a') as f_out:

        first_line = f.readline().rstrip('\n')
        headers = first_line.split(', ')

        for linenr, line in enumerate(f, start=2):
            line = line.rstrip('\n')
            values = line.split(', ')
            d = dict(zip(headers, values))
            if 'ERROR' in d['comment']:
                print(f'{linenr:4} -', line)
                # f_out.write(f'{linenr:4} - ' + line + '\n')
                print(f'{linenr:4} -', line, file=f_out)


