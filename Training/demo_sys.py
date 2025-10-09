import sys

print(sys.version)
print(sys.version_info)
print(f'You are working with Python {sys.version_info.major}')

print(sys.executable)

s = 3.14
print(sys.getsizeof(s))

for p in sys.path:
    print(p)
