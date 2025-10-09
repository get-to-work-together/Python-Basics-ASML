import os

print(sorted(os.listdir()))

print(os.path.exists('demo_numpy.py'))

print('Current working directory', os.getcwd())

os.chdir('..')

print('Current working directory', os.getcwd())
print(sorted(os.listdir()))

