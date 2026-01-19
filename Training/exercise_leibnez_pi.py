n = 100000

total = 0
add = True
for i in range(1, n, 2):
    term = 1 / i
    if add:
        total += term
    else:
        total -= term
    add = not add

pi = total * 4

print(pi)




total = 0
for i in range(1, n, 4):
    total += 1 / i
    total -= 1 / (i + 2)

pi = total * 4

print(pi)
