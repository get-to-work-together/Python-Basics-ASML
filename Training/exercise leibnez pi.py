import math

number_of_iterations = 100_000_00

total = 0
sign = +1

for denominator in range(1, number_of_iterations * 2, 2):
    term = 1 / denominator
    total += sign * term
    sign = -1 * sign

pi = total * 4

print(f'Pi is approximally {pi} after {number_of_iterations} iterations')
print(f'That is almost equal to {math.pi}')

n_accurate_digits = 0
for d1, d2 in zip(str(pi), str(math.pi)):
    if d1 == d2:
        if d1.isdigit():
            n_accurate_digits += 1
    else:
        break

print(f'That is accurate to {n_accurate_digits} digits.')