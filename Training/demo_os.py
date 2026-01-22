import os
from pprint import pprint

print(os.getcwd())

print(os.path.exists('data.txt'))

pprint(sorted(os.listdir()))