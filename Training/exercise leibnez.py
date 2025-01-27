import math

number_of_iterations = 10_000_000

total = 0
sign = +1

for denominator in range(1, number_of_iterations * 2, 2):
    term = 1 / denominator
    total += sign * term
    sign = -1 * sign

pi = total * 4

print(f'Pi is approximally {pi} after {number_of_iterations} iterations')
print(f'That is almost equal to {math.pi}')
