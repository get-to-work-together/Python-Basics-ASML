from pathlib import Path

path = Path(__file__)
print(path)

print(path.parent / 'car.py')
print(path.parent.parent / 'Slides')