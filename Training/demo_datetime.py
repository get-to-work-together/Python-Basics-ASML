import datetime
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR')

birthdate = datetime.date(1956, 8, 20)

print(birthdate.strftime('%A %d %B %Y'))

locale.setlocale(locale.LC_ALL, 'en_US')

today = datetime.date.today()
print(today.strftime('%A %d %B %Y'))

next_week = today + datetime.timedelta(days=7)
print(next_week.strftime('%A %d %B %Y'))