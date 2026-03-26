import sys

print(sys.version)
print(sys.version_info)
print(sys.version_info.major)

print(sys.executable)

for item in sys.path:
    print(item)