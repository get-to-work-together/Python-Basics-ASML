n_iterations = 100000

total = 0
add_term = True
for i in range(1, n_iterations, 2):
    if add_term:
        total += 1/i
    else:
        total -= 1/i
    add_term = not add_term
pi = 4 * total

print('Pi is approximately {}'.format(pi))




total = 0
for i in range(1, n_iterations, 4):
    total = total + 1/i
    total = total - 1/(i + 2)
pi = 4 * total

print('Pi is approximately {}'.format(pi))
