import locale
import datetime

locale.setlocale(locale.LC_ALL, 'nl_nl')

dd = datetime.datetime(2025, 10, 9)

print(dd)

print(dd.strftime('%d-%m-%Y'))
print(dd.strftime('%A %d %B %Y'))