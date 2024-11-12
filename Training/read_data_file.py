filename = 'data.csv'
filename_out = 'out.csv'

with open(filename, mode='r') as f:
    with open(filename_out, mode='a') as f_out:

        headers = f.readline().rstrip('\n').split(',')

        for linenr, line in enumerate(f, start=1):
            columns = line.rstrip('\n').split(',')

            d = dict(zip(headers, columns))

            if int(d['value']) >= 100:
                print(d)

                print(f'{linenr:3}:', d['nr'], d['value'], d['class'], file=f_out)

