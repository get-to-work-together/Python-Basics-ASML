import os

for item in sorted(os.listdir('.')):
    print(item)

print(os.getcwd())
os.chdir('..')
print(os.getcwd())