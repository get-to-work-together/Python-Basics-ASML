import pathlib

print(pathlib.Path.cwd())
print(pathlib.Path(__file__).name)
print(pathlib.Path(__file__).parent.absolute())

filename = '../Training/data.txt'
path = pathlib.Path(filename).resolve(strict=False)
print(path)
print(path)
print(path.name)
print(path.parent)
print(path.parents[0]) # .
print(path.parents[1]) # ..
print(path.parents[2]) # ../..
print(path.parents[-1]) # root

print(path.stat())

print(path.parents[1])

print(path.parents[1] / 'exercises')