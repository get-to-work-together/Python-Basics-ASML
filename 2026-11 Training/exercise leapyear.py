year = int(input('Which year? : '))

can_divide_by_4 = year % 4 == 0
can_divide_by_100 = year % 100 == 0
can_divide_by_400 = year % 400 == 0
is_leapyear = can_divide_by_4 and not can_divide_by_100 or can_divide_by_400

print(year, is_leapyear)

if is_leapyear:
    print(year, 'was a leapyear')
else:
    print(year, 'was not a leapyear')
