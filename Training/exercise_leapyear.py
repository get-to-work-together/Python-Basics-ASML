year = int(input('Enter a year: '))

is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

can_be_divided_by_4 = year % 4 == 0
can_be_divided_by_100 = year % 100 == 0
can_be_divided_by_400 = year % 400 == 0

is_leap = (can_be_divided_by_4 and
           not can_be_divided_by_100 or
           can_be_divided_by_400)

print(year, is_leap)

if is_leap:
    print('Leap year')
else:
    print('Not a leap year')

n_days_in_february = 29 if is_leap else 28

if is_leap:
    n_days_in_february = 29
else:
    n_days_in_february = 28