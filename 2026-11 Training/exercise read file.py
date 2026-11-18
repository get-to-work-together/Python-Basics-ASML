filename_in = 'emails.txtX'
filename_out = 'selected_emails.txt'

try:
    with open(filename_in) as f_in, open(filename_out, mode='w') as f_out:

        for line in f_in.readlines():
            line = line.strip().lower()

            if '@asml' in line:
                print(line, file=f_out)
                q = 10/0

except FileNotFoundError as ex:
    print('Can not open that file', ex)

except ZeroDivisionError as ex:
    print('Can not divide by 0', ex)