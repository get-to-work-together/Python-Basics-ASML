filename = 'ca-500.csv'

# with open(filename) as f:
#     header = f.readline().strip()
#     for line in f:
#         line = line.strip()
#         if 'Montreal' in line:
#             print(line)
#



with open(filename) as f:
    headers = f.readline().strip().split(';')
    for linenr, line in enumerate(f, start=1):
        values = line.strip().split(';')
        d = dict(zip(headers, values))
        if d['city'] == 'Montreal':
            print(linenr, d['first_name'], d['last_name'], d['city'])