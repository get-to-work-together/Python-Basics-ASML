import sys
from pprint import pprint

print(sys.version)
print(sys.version_info)
print(sys.version_info.major)

pprint(sys.path)

print(sys.executable)

n = 2.5
print(sys.getsizeof(n))
n = 2345345345345345345456465645656654565656
print(sys.getsizeof(n))
l = []
print(sys.getsizeof(l))
l = [1,2,3,4,5]
print(sys.getsizeof(l))
