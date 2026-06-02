
year = int(input('Enter a year: '))

isleapyear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(year, isleapyear)


can_divide_by_4 = year % 4 == 0
can_divide_by_100 = year % 100 == 0
can_divide_by_400 = year % 400 == 0
isleapyear = can_divide_by_400 or can_divide_by_4 and not can_divide_by_100

print(year, isleapyear)

if isleapyear:
    print(year, 'is a leapyear')
else:
    print(year, 'is not a leap year')