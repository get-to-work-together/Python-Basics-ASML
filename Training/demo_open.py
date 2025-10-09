filename = 'data.txt'

try:
    with open(filename) as f:

        header = f.readline().strip()
        headers = header.split(';')

        for line in f:
            line = line.strip()
            values = line.split(';')

            d = dict(zip(headers, values))
            print(d)

            if d['id'] == '5':
                print(d['id'], d['name'])
                break

except FileNotFoundError:
    print(f'Cannot open file "{filename}"')

except Exception as ex:
    print('Some went wrong.', ex)
    exit()

