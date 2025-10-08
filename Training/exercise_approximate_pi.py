n = 100_000_000

total = 0
add_term = True
for i in range(1, n, 2):
    term = 1 / i
    if add_term:
        total += term
    else:
        total -= term
    add_term = not add_term

pi = total * 4

print(f'The Leibnez approximation of Pi after {n//2 + 1} iterations is: {pi}')
