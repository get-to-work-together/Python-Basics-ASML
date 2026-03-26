import locale
from datetime import date

locale.setlocale(locale.LC_ALL, 'hu_hu')

dd = date(2000, 1, 1)
print(dd)

print(dd.strftime('%A %d %B %Y'))